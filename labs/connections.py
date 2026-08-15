"""Connection helpers shared by notebooks and exercises.

SQLite is always available. DuckDB and Neon/PostgreSQL are optional and are
opened only when their corresponding lesson needs them.
"""

from __future__ import annotations

import os
import sqlite3
from pathlib import Path

LABS_DIR = Path(__file__).resolve().parent
SQLITE_PATH = LABS_DIR / "database" / "company.sqlite"
DUCKDB_PATH = LABS_DIR / "database" / "analytics.duckdb"

try:
    from dotenv import load_dotenv

    load_dotenv(LABS_DIR / ".env")
except ImportError:
    pass


def sqlite_connection() -> sqlite3.Connection:
    """Return a row-friendly connection to the prepared local database."""
    if not SQLITE_PATH.exists():
        try:
            from setup_lab import build_database
        except ImportError:
            from labs.setup_lab import build_database

        build_database()
    connection = sqlite3.connect(SQLITE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def duckdb_connection():
    """Return the local DuckDB analytical connection when duckdb is installed."""
    try:
        import duckdb
    except ImportError as exc:
        raise RuntimeError("Install lab dependencies: python -m pip install -r labs/requirements.txt") from exc
    return duckdb.connect(str(DUCKDB_PATH))


def neon_connection():
    """Connect to Neon/PostgreSQL through NEON_DATABASE_URL without exposing secrets."""
    database_url = os.getenv("NEON_DATABASE_URL")
    if not database_url:
        raise RuntimeError("Set NEON_DATABASE_URL in your environment before using a Neon lesson.")
    try:
        import psycopg
    except ImportError as exc:
        raise RuntimeError("Install lab dependencies: python -m pip install -r labs/requirements.txt") from exc
    return psycopg.connect(database_url)


def get_connection(engine: str = "sqlite"):
    """Open the database selected for the current exercise."""
    engines = {
        "sqlite": sqlite_connection,
        "duckdb": duckdb_connection,
        "neon": neon_connection,
    }
    try:
        connector = engines[engine.lower()]
    except KeyError as exc:
        raise ValueError(f"Unknown engine {engine!r}. Choose sqlite, duckdb, or neon.") from exc
    return connector()


def query_rows(connection, sql: str, parameters=()) -> list[dict]:
    """Execute a query on SQLite or PostgreSQL and return portable dictionaries."""
    cursor = connection.execute(sql, parameters)
    columns = [description[0] for description in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
