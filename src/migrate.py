import sqlite3
import psycopg2
import json
import logging
import os
import time
from datetime import datetime
from dotenv import load_dotenv

from extract import extract_schema
from transform import convert_type
from load import create_table

# Load environment variables
load_dotenv()

"""
🟦 Module: Database Migration Pipeline

📌 Purpose:
This script performs an end-to-end database migration
from a source SQLite database to a target database
(SQLite/PostgreSQL), including extraction, transformation,
loading, logging, and reporting.

⚙️ Workflow Overview:

1. Load environment variables (.env)
2. Setup logging system (logs/app.log)
3. Read database configuration (db_config.json)
4. Connect to:
   - Source → SQLite
   - Target → SQLite / PostgreSQL
5. Extract schema from source database
6. For each table:
   a. Transform column data types
   b. Create table in target database
   c. Fetch data from source
   d. Insert data into target
7. Track:
   - Total rows processed
   - Errors encountered
8. Generate migration report (reports/report.txt)
9. Log all activities and errors

📂 Project Structure Required:

project/
│
├── data/
│   ├── source.db
│   └── target.db
│
├── config/
│   └── db_config.json
│
├── logs/
│   └── app.log
│
├── reports/
│   └── report.txt
│
├── extract.py     → extract_schema()
├── transform.py   → convert_type()
├── load.py        → create_table()
└── main.py        → run_migration()

📥 Input Files:

1. db_config.json
{
    "source_db": "../data/source.db"
}

2. .env (for PostgreSQL)
DB_HOST=localhost
DB_NAME=mydb
DB_USER=postgres
DB_PASSWORD=secret

📤 Output:

1. Logs File:
   logs/app.log

2. Migration Report:
   reports/report.txt

3. Console Output:
   Migration Done! Rows: X, Errors: Y

🧩 Key Features:

✔ Dynamic schema extraction  
✔ Automatic data type conversion  
✔ Table creation in target DB  
✔ Row-by-row data migration  
✔ Error handling with logging  
✔ Execution time tracking  
✔ Final report generation  

🪵 Logging Levels:

- INFO  → Process steps (connections, inserts, success)
- ERROR → Failures (connection, insert, table errors)

⚠️ Notes:

- Uses '?' placeholders for SQLite
- For PostgreSQL, replace with '%s'
- Ensure correct paths for config, logs, and reports
- Make sure required folders exist or will be created

🚀 Entry Point:

if __name__ == "__main__":
    run_migration()
"""


# Setup logging
os.makedirs('../logs', exist_ok=True)
logging.basicConfig(
    filename='../logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_migration():
    start_time = time.time()
    logging.info("Migration started")

    # Load config
    try:
        with open('../config/db_config.json') as f:
            config = json.load(f)
    except Exception as e:
        logging.error(f"Config error: {e}")
        return

    # Connect SQLite
    try:
        src_conn = sqlite3.connect(config["source_db"])
        src_cursor = src_conn.cursor()
        logging.info("Connected to SQLite")
    except Exception as e:
        logging.error(f"SQLite connection failed: {e}")
        return

    # Connect PostgreSQL
    try:
        # tgt_conn = psycopg2.connect(
        #     host=os.getenv("DB_HOST"),
        #     database=os.getenv("DB_NAME"),
        #     user=os.getenv("DB_USER"),
        #     password=os.getenv("DB_PASSWORD")
        # )
        # logging.info("Connected to PostgreSQL")
        tgt_conn = sqlite3.connect('../data/target.db')
        logging.info("Connected to Target SQLite")
    except Exception as e:
        logging.error(f"PostgreSQL connection failed: {e}")
        return

    total_rows = 0
    errors = 0

    try:
        schema = extract_schema(config["source_db"])
        logging.info(f"Found tables: {list(schema.keys())}")

        for table, columns in schema.items():
            try:
                # Transform schema
                new_columns = [(col[1], convert_type(col[2])) for col in columns]

                # Create table
                create_table(tgt_conn, table, new_columns)

                # Fetch data
                src_cursor.execute(f"SELECT * FROM {table}")
                rows = src_cursor.fetchall()

                cur = tgt_conn.cursor()

                for row in rows:
                    try:
                        # placeholders = ','.join(['%s'] * len(row))
                        # cur.execute(f"INSERT INTO {table} VALUES ({placeholders})", row)
                        placeholders = ','.join(['?'] * len(row))
                        cur.execute(f"INSERT INTO {table} VALUES ({placeholders})", row)
                        total_rows += 1
                        logging.info(f"Inserted row: {row}")
                    except Exception as e:
                        errors += 1
                        logging.error(f"Insert error: {e}")

                tgt_conn.commit()
                logging.info(f"{table} migrated successfully")

            except Exception as e:
                errors += 1
                logging.error(f"Table error {table}: {e}")

    except Exception as e:
        logging.error(f"Migration error: {e}")

    finally:
        src_conn.close()
        tgt_conn.close()

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    # Generate report
    report = f"""
===============================
 DATABASE MIGRATION REPORT
===============================

Migration Date   : {datetime.now().strftime('%Y-%m-%d')}
Source Database  : SQLite
Target Database  : PostgreSQL

-------------------------------
Tables Processed : {len(schema)}
Total Rows       : {total_rows}
Successful Rows  : {total_rows - errors}
Failed Rows      : {errors}

-------------------------------
Status           : {"SUCCESS" if errors == 0 else "PARTIAL SUCCESS"}
Time Taken       : {time_taken} seconds
-------------------------------

Logs File        : logs/app.log
===============================
"""

    os.makedirs('../reports', exist_ok=True)
    with open('../reports/report.txt', 'w') as f:
        f.write(report)

    logging.info("Migration completed")
    print(f"Migration Done! Rows: {total_rows}, Errors: {errors}")


if __name__ == "__main__":
    run_migration()