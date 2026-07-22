"""Migration tests — tmp databases only; never opens backend/data/."""

import os
from pathlib import Path

import pytest
import sqlalchemy as sa
from alembic.config import Config

from alembic import command

BACKEND_DIR = Path(__file__).resolve().parent.parent

CORE_TABLES = {
    "users",
    "assets",
    "downtime_events",
    "work_orders",
    "work_order_transitions",
}


def alembic_config(database_url: str) -> Config:
    """Alembic config pinned to an explicit URL (never the app default)."""
    cfg = Config(str(BACKEND_DIR / "alembic.ini"))
    cfg.set_main_option("script_location", str(BACKEND_DIR / "alembic"))
    cfg.set_main_option("sqlalchemy.url", database_url)
    return cfg


def upgrade_to_head(database_url: str) -> None:
    command.upgrade(alembic_config(database_url), "head")


def test_upgrade_creates_all_tables_on_sqlite(tmp_path: Path) -> None:
    url = f"sqlite:///{tmp_path / 'migrations.db'}"
    upgrade_to_head(url)

    engine = sa.create_engine(url)
    try:
        inspector = sa.inspect(engine)
        tables = set(inspector.get_table_names())
        assert CORE_TABLES <= tables

        # The FS-Q1 partial unique index must exist and be unique.
        indexes = inspector.get_indexes("downtime_events")
        ongoing = [
            ix
            for ix in indexes
            if ix["name"] == "uq_downtime_events_ongoing_per_asset"
        ]
        assert len(ongoing) == 1
        assert ongoing[0]["unique"]
    finally:
        engine.dispose()


def test_upgrade_runs_on_postgres_when_url_provided() -> None:
    url = os.environ.get("CMMESS_TEST_POSTGRES_URL")
    if not url:
        pytest.skip(
            "CMMESS_TEST_POSTGRES_URL not set — dual-engine Postgres "
            "migration check skipped (DEC-006)"
        )

    cfg = alembic_config(url)
    command.upgrade(cfg, "head")
    engine = sa.create_engine(url)
    try:
        inspector = sa.inspect(engine)
        assert CORE_TABLES <= set(inspector.get_table_names())
    finally:
        engine.dispose()
        # Leave the designated test database clean for reruns.
        command.downgrade(cfg, "base")
