"""Model round-trips and DB-level constraint proofs on migrated tmp SQLite.

Never opens backend/data/ — every test runs against a tmp_path database.
"""

from collections.abc import Iterator
from datetime import UTC, datetime
from pathlib import Path

import pytest
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import (
    Asset,
    AssetProvenance,
    DowntimeEvent,
    DowntimeProducer,
    User,
    UserRole,
    WorkOrder,
    WorkOrderOrigin,
    WorkOrderPriority,
    WorkOrderStatus,
    WorkOrderTransition,
)
from tests.test_migrations import upgrade_to_head


@pytest.fixture()
def session(tmp_path: Path) -> Iterator[Session]:
    """A session on a freshly migrated tmp SQLite database."""
    url = f"sqlite:///{tmp_path / 'models.db'}"
    upgrade_to_head(url)
    engine = sa.create_engine(url)
    with Session(engine) as sess:
        yield sess
    engine.dispose()


def _now() -> datetime:
    return datetime.now(UTC)


def _make_asset(session: Session, path: str = "plant/area/line/asset-1") -> Asset:
    asset = Asset(
        path=path,
        display_name="Asset One",
        provenance=AssetProvenance.MANUAL,
    )
    session.add(asset)
    session.flush()
    return asset


def test_round_trip_all_entities(session: Session) -> None:
    user = User(
        username="planner1", role=UserRole.PLANNER, password_hash="not-a-real-hash"
    )
    asset = _make_asset(session)
    session.add(user)
    session.flush()

    event = DowntimeEvent(
        asset_id=asset.id,
        producer=DowntimeProducer.MANUAL,
        down_at=_now(),
        up_at=_now(),
        reported_by=user.id,
    )
    session.add(event)
    session.flush()

    wo = WorkOrder(
        asset_id=asset.id,
        origin=WorkOrderOrigin.MANUAL,
        title="Fix the thing",
        created_by=user.id,
    )
    session.add(wo)
    session.flush()

    transition = WorkOrderTransition(
        work_order_id=wo.id,
        from_status=WorkOrderStatus.OPEN,
        to_status=WorkOrderStatus.PLANNED,
        at=_now(),
        by_user=user.id,
    )
    session.add(transition)
    session.commit()

    loaded_user = session.get(User, user.id)
    loaded_asset = session.get(Asset, asset.id)
    loaded_event = session.get(DowntimeEvent, event.id)
    loaded_wo = session.get(WorkOrder, wo.id)
    loaded_transition = session.get(WorkOrderTransition, transition.id)
    assert loaded_user is not None and loaded_user.role is UserRole.PLANNER
    assert loaded_asset is not None
    assert loaded_asset.provenance is AssetProvenance.MANUAL
    assert loaded_asset.retired is False
    assert loaded_event is not None and loaded_event.up_at is not None
    assert loaded_wo is not None
    assert loaded_wo.priority is WorkOrderPriority.MEDIUM
    assert loaded_wo.status is WorkOrderStatus.OPEN
    assert loaded_wo.downtime_event_id is None
    assert loaded_transition is not None
    assert loaded_transition.to_status is WorkOrderStatus.PLANNED


def test_second_ongoing_downtime_event_rejected_fs_q1(session: Session) -> None:
    asset = _make_asset(session)
    first = DowntimeEvent(
        asset_id=asset.id, producer=DowntimeProducer.UNS, down_at=_now()
    )
    session.add(first)
    session.commit()

    # Second ongoing event on the same asset: rejected at the DB level.
    session.add(
        DowntimeEvent(asset_id=asset.id, producer=DowntimeProducer.UNS, down_at=_now())
    )
    with pytest.raises(IntegrityError):
        session.commit()
    session.rollback()

    # End the first event; a new ongoing event is then accepted.
    ended = session.get(DowntimeEvent, first.id)
    assert ended is not None
    ended.up_at = _now()
    session.commit()

    session.add(
        DowntimeEvent(asset_id=asset.id, producer=DowntimeProducer.UNS, down_at=_now())
    )
    session.commit()
    count = session.scalar(
        sa.select(sa.func.count()).select_from(DowntimeEvent).where(
            DowntimeEvent.asset_id == asset.id
        )
    )
    assert count == 2


def test_origin_event_pairing_rejected_both_ways(session: Session) -> None:
    asset = _make_asset(session)
    event = DowntimeEvent(
        asset_id=asset.id,
        producer=DowntimeProducer.UNS,
        down_at=_now(),
        up_at=_now(),
    )
    session.add(event)
    session.commit()

    # manual origin must NOT carry a downtime event.
    session.add(
        WorkOrder(
            asset_id=asset.id,
            origin=WorkOrderOrigin.MANUAL,
            downtime_event_id=event.id,
            title="Illegal: manual origin with event",
        )
    )
    with pytest.raises(IntegrityError):
        session.commit()
    session.rollback()

    # downtime origins MUST carry a downtime event.
    session.add(
        WorkOrder(
            asset_id=asset.id,
            origin=WorkOrderOrigin.UNS_DOWNTIME,
            title="Illegal: downtime origin without event",
        )
    )
    with pytest.raises(IntegrityError):
        session.commit()
    session.rollback()

    # Both legal pairings are accepted.
    session.add(
        WorkOrder(
            asset_id=asset.id,
            origin=WorkOrderOrigin.UNS_DOWNTIME,
            downtime_event_id=event.id,
            title="Legal: downtime origin with event",
        )
    )
    session.add(
        WorkOrder(
            asset_id=asset.id,
            origin=WorkOrderOrigin.MANUAL,
            title="Legal: manual origin without event",
        )
    )
    session.commit()
