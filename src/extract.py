import sqlite3

"""
# Function: extract_schema(db_path)

# Purpose:
Extracts the complete schema (structure) of all tables
from a SQLite database.

# Steps Performed:

1. Connect to the SQLite database using the given path
2. Fetch all table names from 'sqlite_master'
3. Loop through each table:
   - Use PRAGMA table_info(table_name)
   - Get column details for that table
4. Store results in a dictionary:
   {
       'table_name': [column_details, ...]
   }
5. Close the database connection
6. Print and return the schema

# Output Example:
{
    'users': [
        (0, 'id', 'INTEGER', 0, None, 1),
        (1, 'name', 'TEXT', 0, None, 0),
        (2, 'age', 'INTEGER', 0, None, 0)
    ]
}

# Column Tuple Format:
(cid, name, type, notnull, default_value, pk)

- cid           → Column index
- name          → Column name
- type          → Data type
- notnull       → NOT NULL constraint (0 = No, 1 = Yes)
- default_value → Default value
- pk            → Primary key (1 = Yes, 0 = No)
"""

def extract_schema(db_path):
    # 1. Connect to the SQLite database using the given path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # 2. Fetch all table names from 'sqlite_master'
    tables = cursor.fetchall()
    # print(tables)

    schema = {}
    #  3. Loop through each table:
    # - Use PRAGMA table_info(table_name)
    # - Get column details for that table
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        schema[table_name] = cursor.fetchall()
    #  4. Store results in a dictionary:
    # {
    #     'table_name': [column_details, ...]
    # }
    # 5. Close the database connection
    conn.close()
    # 6. Print and return the schema
    print(schema)
    # output: {'users': [(0, 'id', 'INTEGER', 0, None, 1), (1, 'name', 'TEXT', 0, None, 0), (2, 'age', 'INTEGER', 0, None, 0)]}
    return schema

# extract_schema('../data/source.db')