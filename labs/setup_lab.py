"""Build the local SQLite lab database from versioned source files."""

from __future__ import annotations

import csv
import sqlite3
from pathlib import Path

LABS_DIR = Path(__file__).resolve().parent
DATA_DIR = LABS_DIR / "data"
DATABASE_DIR = LABS_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "company.sqlite"
SCHEMA_PATH = LABS_DIR / "sql" / "schema.sql"

TABLE_FILES = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "payments": "payments.csv",
}

INTEGER_COLUMNS = {
    "customer_id",
    "product_id",
    "order_id",
    "order_item_id",
    "payment_id",
    "quantity",
}
REAL_COLUMNS = {"unit_price", "amount"}


def convert_value(column: str, value: str):
    if value == "":
        return None
    if column in INTEGER_COLUMNS:
        return int(value)
    if column in REAL_COLUMNS:
        return float(value)
    return value


def load_csv(connection: sqlite3.Connection, table: str, filename: str) -> int:
    with (DATA_DIR / filename).open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        rows = [
            {column: convert_value(column, value) for column, value in row.items()}
            for row in reader
        ]
    if not rows:
        return 0
    columns = list(rows[0])
    placeholders = ", ".join("?" for _ in columns)
    connection.executemany(
        f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})",
        [[row[column] for column in columns] for row in rows],
    )
    return len(rows)


def build_database() -> Path:
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    try:
        connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        counts = {
            table: load_csv(connection, table, filename)
            for table, filename in TABLE_FILES.items()
        }
        connection.executemany(
            """
            INSERT INTO pipeline_runs
                (run_id, pipeline_name, started_at, finished_at, rows_read, rows_written, status, error_message)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (1, "daily_orders", "2025-06-08T01:00:00Z", "2025-06-08T01:02:18Z", 12, 12, "success", None),
                (2, "payment_events", "2025-06-08T01:05:00Z", "2025-06-08T01:05:41Z", 6, 5, "failed", "Malformed event evt-006"),
                (3, "customer_snapshot", "2025-06-08T02:00:00Z", "2025-06-08T02:00:29Z", 8, 8, "success", None),
            ],
        )
        connection.commit()
    finally:
        connection.close()
    print(f"Created {DATABASE_PATH}")
    print("Loaded " + ", ".join(f"{table}={count}" for table, count in counts.items()))
    return DATABASE_PATH


if __name__ == "__main__":
    build_database()
