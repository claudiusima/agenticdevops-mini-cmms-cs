"""Backend configuration from environment. No secrets in code."""

import os
from pathlib import Path

ENV_DATABASE_URL = "CMMESS_DATABASE_URL"

_BACKEND_DIR = Path(__file__).resolve().parent.parent


def default_sqlite_path() -> Path:
    """Path of the default dev SQLite database (gitignored)."""
    return _BACKEND_DIR / "data" / "cmmess.db"


def get_database_url() -> str:
    """Database URL from ``CMMESS_DATABASE_URL``, else the dev SQLite file.

    The default's parent directory is created lazily here — only when the
    default is actually used, never as an import side effect.
    """
    url = os.environ.get(ENV_DATABASE_URL)
    if url:
        return url
    path = default_sqlite_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    return f"sqlite:///{path}"
