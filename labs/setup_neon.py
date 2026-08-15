"""Load the versioned lab dataset into an optional Neon/PostgreSQL database."""

from __future__ import annotations

import csv
from pathlib import Path

from connections import neon_connection

LABS_DIR = Path(__file__).resolve().parent
DATA_DIR = LABS_DIR / "data"
SCHEMA_PATH = LABS_DIR / "sql" / "neon_schema.sql"
TABLE_FILES = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "payments": "payments.csv",
}


def load_csv(cursor, table: str, filename: str) -> int:
    with (DATA_DIR / filename).open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        rows = list(reader)
    if not rows:
        return 0
    columns = list(rows[0])
    placeholders = ", ".join("%s" for _ in columns)
    cursor.executemany(
        f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})",
        [[row[column] or None for column in columns] for row in rows],
    )
    return len(rows)


def build_neon_database() -> None:
    connection = neon_connection()
    try:
        with connection.cursor() as cursor:
            schema = SCHEMA_PATH.read_text(encoding="utf-8")
            for statement in schema.split(";"):
                if statement.strip():
                    cursor.execute(statement)
            counts = {
                table: load_csv(cursor, table, filename)
                for table, filename in TABLE_FILES.items()
            }
            cursor.executemany(
                """
                INSERT INTO pipeline_runs
                    (run_id, pipeline_name, started_at, finished_at, rows_read, rows_written, status, error_message)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
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
    print("Neon/PostgreSQL lab loaded: " + ", ".join(f"{table}={count}" for table, count in counts.items()))


if __name__ == "__main__":
    build_neon_database()
