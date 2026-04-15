import sqlite3

# check data in new database
# conn = sqlite3.connect('data/target.db')
# cur = conn.cursor()

# # cur.execute("SELECT * FROM users")
# cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cur.fetchall())

# =========================================================

# create the new table and database

conn = sqlite3.connect('data/source.db')
cur = conn.cursor()

# cur.execute("""
# CREATE TABLE users (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER
# )
# """)

# cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
# cur.execute("INSERT INTO users (name, age) VALUES ('Bob', 30)")
# cur.execute("DROP TABLE customers")
# cur.execute("DROP TABLE orders")
# cur.execute("DROP TABLE products")
# cur.execute("DROP TABLE order_items")
# cur.execute("DROP TABLE payments")
# cur.execute("DROP TABLE returns")
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())


# conn.commit()
# conn.close()

