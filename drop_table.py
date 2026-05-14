import sqlite3

target_conn = sqlite3.connect('data/target.db')
target_cur = target_conn.cursor()

source_conn = sqlite3.connect('data/source.db')
source_cur = source_conn.cursor()

target_cur.execute("DROP TABLE customers")
target_cur.execute("DROP TABLE orders")
target_cur.execute("DROP TABLE products")
target_cur.execute("DROP TABLE order_items")
target_cur.execute("DROP TABLE payments")
target_cur.execute("DROP TABLE returns")