# Local Data Engineering Lab

This laboratory keeps practical SQL and Python work inside the repository. It uses one small business dataset across multiple storage engines so lessons remain coherent.

## Engines

| Engine | Use | Availability |
| --- | --- | --- |
| SQLite | SQL foundations, joins, transactions, Python database access | Ready locally with no installation |
| DuckDB | Analytical SQL, CSV and Parquet queries | Optional dependency |
| Neon/PostgreSQL | PostgreSQL-specific syntax and cloud database exercises | Optional account and environment variable |

## Quick start

From the repository root:

```bash
python3 labs/setup_lab.py
python3 -m pip install -r labs/requirements.txt
jupyter notebook labs/python/01_data_engineering_workbook.ipynb
```

The database is already generated in `labs/database/company.sqlite`. Running `setup_lab.py` safely rebuilds it from the versioned CSV files.

## Data model

```text
customers 1 ── * orders 1 ── * order_items * ── 1 products
                       1 ── * payments

pipeline_runs records operational execution history.
events.jsonl simulates an event-stream source.
```

## Choosing a database in Python

```python
from connections import get_connection

connection = get_connection("sqlite")
# connection = get_connection("duckdb")
# connection = get_connection("neon")
```

SQLite is the default. Use DuckDB for analytical/file exercises. Use Neon only when a lesson requires real PostgreSQL behavior.

## Neon setup

1. Copy `labs/.env.example` to `labs/.env`.
2. Put the real connection string in `NEON_DATABASE_URL`.
3. Never commit `labs/.env`.
4. Load the variable in the terminal before starting Jupyter, or use a local environment manager.
5. Run `python3 labs/setup_neon.py` once to load the same sample company data into Neon.

No password or connection string is included in this repository.

## Rebuilding generated files

```bash
python3 labs/setup_lab.py
```

The source of truth is `labs/data/*.csv` plus `labs/sql/schema.sql`. The SQLite file is a ready-to-use generated artifact.
