"""SQLAlchemy engine and session factory built from config.

Nothing in this module connects to, creates, or migrates a database at
import time — the engine is constructed lazily on first use, so importing
the app never touches storage.
"""

from functools import lru_cache
from typing import Any

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import Session, sessionmaker

from app.config import get_database_url


def _enable_sqlite_foreign_keys(dbapi_connection: Any, _connection_record: Any) -> None:
    """SQLite does not enforce foreign keys unless asked per connection.

    Postgres always enforces them; without this pragma the two engines would
    silently diverge on referential integrity (dual-engine parity, DEC-006).
    """
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


@lru_cache(maxsize=1)
def get_engine() -> Engine:
    """The process-wide engine for the configured database URL."""
    engine = create_engine(get_database_url())
    if engine.dialect.name == "sqlite":
        event.listen(engine, "connect", _enable_sqlite_foreign_keys)
    return engine


@lru_cache(maxsize=1)
def get_session_factory() -> sessionmaker[Session]:
    """Typed session factory bound to the process-wide engine."""
    return sessionmaker(bind=get_engine())
