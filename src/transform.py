"""
# Function: convert_type(sqlite_type)

# Purpose:
Converts SQLite data types into compatible types
(for another database like MySQL/PostgreSQL).

# How It Works:

1. Takes a SQLite data type as input (e.g., "INTEGER", "TEXT", "REAL")
2. Uses a mapping dictionary to convert it:
   - INTEGER → INTEGER
   - TEXT    → VARCHAR
   - REAL    → FLOAT
3. If the type is not found in mapping,
   it returns "VARCHAR" as the default

# Input:
sqlite_type (str) → SQLite column type

# Output:
str → Converted data type

# Examples:
convert_type("INTEGER") → "INTEGER"
convert_type("TEXT")    → "VARCHAR"
convert_type("REAL")    → "FLOAT"
convert_type("BLOB")    → "VARCHAR" (default)
"""

def convert_type(sqlite_type):
    mapping = {
        "INTEGER": "INTEGER",
        "TEXT": "VARCHAR",
        "REAL": "FLOAT"
    }

    return mapping.get(sqlite_type.upper(), "VARCHAR")