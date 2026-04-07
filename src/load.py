import logging
"""
# Function: create_table(conn, table_name, columns)

# Purpose:
Creates a table in the database dynamically using
the provided table name and column definitions.

# How It Works:

1. Creates a cursor object from the database connection
2. Prepares column definitions:
   - Each column is formatted as: "column_name data_type"
3. Builds a SQL query:
   CREATE TABLE IF NOT EXISTS table_name (columns...)
4. Executes the query
5. Commits the changes to the database
6. Logs success or error messages

# Input Parameters:
- conn (object)       → Database connection
- table_name (str)    → Name of the table to create
- columns (list)      → List of tuples:
                        [(column_name, data_type), ...]

# Output:
- No return value
- Table is created in the database
- Logs success or error message

# Example Input:
table_name = "users"
columns = [
    ("id", "INTEGER"),
    ("name", "VARCHAR"),
    ("age", "INTEGER")
]

# Example Query Generated:
CREATE TABLE IF NOT EXISTS users (id INTEGER, name VARCHAR, age INTEGER);

# Logging:
- INFO  → Table created successfully
- ERROR → If any exception occurs during execution
"""
def create_table(conn, table_name, columns):
    try:
        cur = conn.cursor()

        col_defs = [f"{col[0]} {col[1]}" for col in columns]
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(col_defs)});"

        cur.execute(query)
        conn.commit()

        logging.info(f"Table '{table_name}' created successfully")
    
    except Exception as e:
        logging.error(f"Error creating table {table_name}: {e}")