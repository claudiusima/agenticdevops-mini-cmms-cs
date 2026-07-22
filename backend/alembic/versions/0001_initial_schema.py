"""Initial core schema: users, assets, downtime_events, work_orders,
work_order_transitions.

Dual-engine (DEC-006): this file runs unmodified on SQLite and Postgres —
no dialect-specific SQL, no native ENUM types. Enum-valued columns are
strings with CHECK constraints; the FS-Q1 "one ongoing downtime event per
asset" rule is a partial unique index; the FS §5 work-order origin↔event
pairing is a table CHECK.

Revision ID: 0001
Revises:
Create Date: 2026-07-22

"""

import sqlalchemy as sa

from alembic import op

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("username", sa.String(length=64), nullable=False),
        sa.Column("role", sa.String(length=32), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.CheckConstraint("role IN ('user', 'planner')", name="ck_users_user_role"),
        sa.UniqueConstraint("username", name="uq_users_username"),
    )

    op.create_table(
        "assets",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("path", sa.String(length=255), nullable=False),
        sa.Column("display_name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("provenance", sa.String(length=32), nullable=False),
        sa.Column("retired", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.CheckConstraint(
            "provenance IN ('uns_discovered', 'manual')",
            name="ck_assets_asset_provenance",
        ),
        sa.UniqueConstraint("path", name="uq_assets_path"),
    )

    op.create_table(
        "downtime_events",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("asset_id", sa.Integer(), nullable=False),
        sa.Column("producer", sa.String(length=32), nullable=False),
        sa.Column("down_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("up_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("reported_by", sa.Integer(), nullable=True),
        sa.Column("ended_by", sa.Integer(), nullable=True),
        sa.CheckConstraint(
            "producer IN ('uns', 'manual')",
            name="ck_downtime_events_downtime_producer",
        ),
        sa.ForeignKeyConstraint(
            ["asset_id"], ["assets.id"], name="fk_downtime_events_asset_id_assets"
        ),
        sa.ForeignKeyConstraint(
            ["reported_by"], ["users.id"], name="fk_downtime_events_reported_by_users"
        ),
        sa.ForeignKeyConstraint(
            ["ended_by"], ["users.id"], name="fk_downtime_events_ended_by_users"
        ),
    )
    # FS-Q1: at most one ongoing downtime event per asset, at the DB level.
    # Partial unique indexes are supported by both SQLite and Postgres; the
    # WHERE clause is identical SQL on both engines.
    op.create_index(
        "uq_downtime_events_ongoing_per_asset",
        "downtime_events",
        ["asset_id"],
        unique=True,
        sqlite_where=sa.text("up_at IS NULL"),
        postgresql_where=sa.text("up_at IS NULL"),
    )

    op.create_table(
        "work_orders",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("asset_id", sa.Integer(), nullable=False),
        sa.Column("origin", sa.String(length=32), nullable=False),
        sa.Column("downtime_event_id", sa.Integer(), nullable=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column(
            "priority", sa.String(length=32), nullable=False, server_default="medium"
        ),
        sa.Column(
            "status", sa.String(length=32), nullable=False, server_default="open"
        ),
        sa.Column("created_by", sa.Integer(), nullable=True),
        sa.Column("assigned_to", sa.Integer(), nullable=True),
        sa.Column("scheduled_start", sa.DateTime(timezone=True), nullable=True),
        sa.Column("expected_duration_minutes", sa.Integer(), nullable=True),
        sa.Column("completion_notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.CheckConstraint(
            "origin IN ('uns_downtime', 'manual_downtime', 'manual')",
            name="ck_work_orders_work_order_origin",
        ),
        sa.CheckConstraint(
            "priority IN ('low', 'medium', 'high')",
            name="ck_work_orders_work_order_priority",
        ),
        sa.CheckConstraint(
            "status IN ('open', 'planned', 'in_progress', 'completed', 'cancelled')",
            name="ck_work_orders_work_order_status",
        ),
        # FS §5 pairing: manual origin ⇔ no downtime event; downtime
        # origins ⇔ a downtime event.
        sa.CheckConstraint(
            "(origin = 'manual' AND downtime_event_id IS NULL) OR "
            "(origin IN ('uns_downtime', 'manual_downtime') "
            "AND downtime_event_id IS NOT NULL)",
            name="ck_work_orders_origin_event_pairing",
        ),
        sa.ForeignKeyConstraint(
            ["asset_id"], ["assets.id"], name="fk_work_orders_asset_id_assets"
        ),
        sa.ForeignKeyConstraint(
            ["downtime_event_id"],
            ["downtime_events.id"],
            name="fk_work_orders_downtime_event_id_downtime_events",
        ),
        sa.ForeignKeyConstraint(
            ["created_by"], ["users.id"], name="fk_work_orders_created_by_users"
        ),
        sa.ForeignKeyConstraint(
            ["assigned_to"], ["users.id"], name="fk_work_orders_assigned_to_users"
        ),
    )

    op.create_table(
        "work_order_transitions",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("work_order_id", sa.Integer(), nullable=False),
        sa.Column("from_status", sa.String(length=32), nullable=False),
        sa.Column("to_status", sa.String(length=32), nullable=False),
        sa.Column("at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("by_user", sa.Integer(), nullable=True),
        sa.Column("note", sa.Text(), nullable=True),
        sa.CheckConstraint(
            "from_status IN "
            "('open', 'planned', 'in_progress', 'completed', 'cancelled')",
            name="ck_work_order_transitions_from_status",
        ),
        sa.CheckConstraint(
            "to_status IN "
            "('open', 'planned', 'in_progress', 'completed', 'cancelled')",
            name="ck_work_order_transitions_to_status",
        ),
        sa.ForeignKeyConstraint(
            ["work_order_id"],
            ["work_orders.id"],
            name="fk_work_order_transitions_work_order_id_work_orders",
        ),
        sa.ForeignKeyConstraint(
            ["by_user"], ["users.id"], name="fk_work_order_transitions_by_user_users"
        ),
    )


def downgrade() -> None:
    op.drop_table("work_order_transitions")
    op.drop_table("work_orders")
    op.drop_index("uq_downtime_events_ongoing_per_asset", table_name="downtime_events")
    op.drop_table("downtime_events")
    op.drop_table("assets")
    op.drop_table("users")
