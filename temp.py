import sqlite3

# check data in new database
conn = sqlite3.connect('data/target.db')
cur = conn.cursor()

cur.execute("SELECT * FROM users")
print(cur.fetchall())

# =========================================================

# create the new table and database

# conn = sqlite3.connect('data/source.db')
# cur = conn.cursor()

# cur.execute("""
# CREATE TABLE users (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER
# )
# """)

# cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
# cur.execute("INSERT INTO users (name, age) VALUES ('Bob', 30)")

# conn.commit()
# conn.close()

