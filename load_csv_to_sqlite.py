import sqlite3
import pandas as pd
import time
start = time.time()

orders_df = pd.read_csv('sample_data\\orders.csv')
customers_df = pd.read_csv('sample_data\\customers.csv')
products_df = pd.read_csv('sample_data\\products.csv')
order_items_df = pd.read_csv('sample_data\\order_items.csv')
payments_df = pd.read_csv('sample_data\\payments.csv')
returns_df = pd.read_csv('sample_data\\returns.csv')

# Function to print a separator line
def print_line(length=70, char='-'):
    print(char * length)

print_line() 
print("ETL Process Started: Generating data and loading into database...")
print_line()
print()

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect('data/source.db')
cur = conn.cursor()

print("\n📊 Available Tables in Database:")
print_line(40, "-")

# SQL query to fetch all table names from SQLite system table
cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
tables  = cur.fetchall()
for i, table in enumerate(tables, start=1):
    print(f"{i:>2}. {table[0]}")

print_line(40, "-")
print()

# Function to clean string values for SQL
def clean_str(val):
    if pd.isna(val):
        return "NULL"
    val = str(val).replace("'", "''")  # escape single quotes
    return f"'{val}'"

def clean_num(val):
    if pd.isna(val):
        return "NULL"
    return str(val)


print("Data Insertion Started...")

# There is Inserting Orders table data
print("Inserting into Orders...")

# order_id,customer_id,order_date,order_status,channel,coupon_code,order_total
# 1,476,2025-07-06 00:49:18,shipped,mobile,,4828.06

for _, row in orders_df.iterrows():
    cur.execute(
        f"INSERT INTO orders VALUES ("
        f"{clean_num(row['order_id'])}, "
        f"{clean_num(row['customer_id'])}, "
        f"{clean_str(row['order_date'])}, "
        f"{clean_str(row['order_status'])}, "
        f"{clean_str(row['channel'])}, "
        f"{clean_str(row['coupon_code'])}, "
        f"{clean_num(row['order_total'])}"
        f");"
    )
conn.commit()
cur.execute("SELECT count(*) FROM ORDERS")
print(f"{cur.fetchall()[0][0]} records inserted")
print()

# There is Inserting Customers table data
print("Inserting into Customers...")
# customer_id,customer_name,email,city,state,signup_date,tier
# 1,Ishita Patil,ishita.patil1@mail.com,Hyderabad,TS,2025-08-08,bronze

for _, row in customers_df.iterrows():
    cur.execute(
        f"INSERT INTO customers VALUES ("
        f"{clean_num(row['customer_id'])}, "
        f"{clean_str(row['customer_name'])}, "
        f"{clean_str(row['email'])}, "
        f"{clean_str(row['city'])}, "
        f"{clean_str(row['state'])}, "
        f"{clean_str(row['signup_date'])}, "
        f"{clean_str(row['tier'])}"
        f");"
    )
conn.commit()
cur.execute("SELECT count(*) FROM customers")
print(f"{cur.fetchall()[0][0]} records inserted")
print()

# There is Inserting Products table data
print("Inserting into Products...")
# product_id,product_name,category,brand,price
# 1,Orbit-Boo-1,Books,Orbit,33616.44

for _, row in products_df.iterrows():
    cur.execute(
        f"INSERT INTO products VALUES ("
        f"{clean_num(row['product_id'])}, "
        f"{clean_str(row['product_name'])}, "
        f"{clean_str(row['category'])}, "
        f"{clean_str(row['brand'])}, "
        f"{clean_num(row['price'])}"
        f");"
    )

conn.commit()
cur.execute("SELECT count(*) FROM products")
print(f"{cur.fetchall()[0][0]} records inserted")
print()


# There is Inserting Order_items table data
print("Inserting into Order_items...")

# order_item_id,order_id,product_id,quantity,unit_price,line_amount
# 1,2673,292,1,26690.24,26690.24

for _, row in order_items_df.iterrows():
    cur.execute(
        f"INSERT INTO order_items VALUES ("
        f"{clean_num(row['order_item_id'])}, "
        f"{clean_num(row['order_id'])}, "
        f"{clean_num(row['product_id'])}, "
        f"{clean_num(row['quantity'])}, "
        f"{clean_num(row['unit_price'])}, "
        f"{clean_num(row['line_amount'])}"
        f");"
    )

conn.commit()
cur.execute("SELECT count(*) FROM order_items")
print(f"{cur.fetchall()[0][0]} records inserted")
print()


# There is Inserting Payments table data
print("Inserting into Payments...")

# payment_id,order_id,payment_method,payment_status,paid_amount,payment_time
# 1,2702,netbanking,success,7309.02,2025-05-01 20:48:18
df = pd.read_csv('sample_data\\payments.csv')

for _, row in df.iterrows():
    cur.execute(
        f"INSERT INTO payments VALUES ("
        f"{clean_num(row['payment_id'])}, "
        f"{clean_num(row['order_id'])}, "
        f"{clean_str(row['payment_method'])}, "
        f"{clean_str(row['payment_status'])}, "
        f"{clean_num(row['paid_amount'])}, "
        f"{clean_str(row['payment_time'])}"
        f");"
    )

conn.commit()
cur.execute("SELECT count(*) FROM payments")
print(f"{cur.fetchall()[0][0]} records inserted")
print()


# There is Inserting Returns table data
print("Inserting into Returns...")

# return_id,order_id,reason,return_date,refund_amount
# 1,5923,late_delivery,2025-05-12,7575.85

for _, row in returns_df.iterrows():
    cur.execute(
        f"INSERT INTO returns VALUES ("
        f"{clean_num(row['return_id'])}, "
        f"{clean_num(row['order_id'])}, "
        f"{clean_str(row['reason'])}, "
        f"{clean_str(row['return_date'])}, "
        f"{clean_num(row['refund_amount'])} "
        f");"
    )

conn.commit()
cur.execute("SELECT count(*) FROM returns")
print(f"{cur.fetchall()[0][0]} records inserted")
print()

print_line()
print("✅ ETL Process Completed Successfully")
print_line()

end = time.time()
print(f"\n⏱️ Total Time: {round(end - start, 2)} seconds")

conn.close()