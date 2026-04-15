import sqlite3

conn = sqlite3.connect('data/source.db')
cur = conn.cursor()

def print_line(length=70, char='-'):
    print(char * length)

# Function to print section title
def print_section(title):
    print(f"\n➡️ {title}...")

# Function to print success message
def print_success(message):
    print(f"   ✔ {message}")

print_line()
print("Database Setup Started...")
print_line()
# Enable foreign keys (IMPORTANT in SQLite)
cur.execute("PRAGMA foreign_keys = ON;")

print("\nCreating Tables...")

print_section("Creating table: customers")
# Customers Table
cur.execute("""
CREATE TABLE customers (
    customer_id   INTEGER PRIMARY KEY,
    customer_name TEXT,
    email         TEXT,
    city          TEXT,
    state         TEXT,
    signup_date   TEXT,
    tier          TEXT
);
""")
print_success("customers table created successfully")

print_section("Creating table: orders")
# Orders Table
cur.execute("""
CREATE TABLE orders (
    order_id     INTEGER PRIMARY KEY,
    customer_id  INTEGER,
    order_date   TEXT,
    order_status TEXT,
    channel      TEXT,
    coupon_code  TEXT,
    order_total  REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
""")
print_success("orders table created successfully")


print_section("Creating table: products")
# Products Table
cur.execute("""
CREATE TABLE products (
    product_id   INTEGER PRIMARY KEY,
    product_name TEXT,
    category     TEXT,
    brand        TEXT,
    price        REAL
);
""")
print_success("products table created successfully")


print_section("Creating table: order_items")
# Order Items Table
cur.execute("""
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id      INTEGER,
    product_id    INTEGER,
    quantity      INTEGER,
    unit_price    REAL,
    line_amount   REAL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
""")
print_success("order_items table created successfully")


print_section("Creating table: payments")
# Payments Table
cur.execute("""
CREATE TABLE payments (
    payment_id     INTEGER PRIMARY KEY,
    order_id       INTEGER,
    payment_method TEXT,
    payment_status TEXT,
    paid_amount    REAL,
    payment_time   TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
""")
print_success("payments table created successfully")


print_section("Creating table: returns")
# Returns Table
cur.execute("""
CREATE TABLE returns (
    return_id     INTEGER PRIMARY KEY,
    order_id      INTEGER,
    reason        TEXT,
    return_date   TEXT,
    refund_amount REAL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
""")
print_success("returns table created successfully")

conn.commit()

print_line()
print("Database Setup Completed Successfully")
print_line()

conn.close()