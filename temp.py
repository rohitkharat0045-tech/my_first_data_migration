import sqlite3

# check data in new database
target_conn = sqlite3.connect('data/target.db')
target_cur = target_conn.cursor()

source_conn = sqlite3.connect('data/source.db')
source_cur = source_conn.cursor()

# target_cur.execute("DROP TABLE customers")
# target_cur.execute("DROP TABLE orders")
# target_cur.execute("DROP TABLE products")
# target_cur.execute("DROP TABLE order_items")
# target_cur.execute("DROP TABLE payments")
# target_cur.execute("DROP TABLE returns")

# =========================================================
def target_database(target_conn,target_cur):
    print("\n" + "="*50)
    print("         TARGET DATABASE SUMMARY")
    print("="*50)

    # Get tables
    target_cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    target_tables = [i[0] for i in target_cur.fetchall()]

    # ✅ If no tables exist
    if len(target_tables) == 0:
        print("\n⚠️ No tables found in target database.")
        print("="*50 + "\n")

    else:
        print(f"\nTotal Tables: {len(target_tables)}")
        print("-"*50)

    # Header
    print(f"{'TABLE NAME':<25} | {'ROWS':>10}")
    print("-"*50)

    total_rows = 0

    for table in target_tables:
        target_cur.execute(f"SELECT COUNT(*) FROM {table}")
        count = target_cur.fetchone()[0]
        total_rows += count

        print(f"{table:<25} | {count:>10}")

    print("-"*50)
    print(f"{'TOTAL':<25} | {total_rows:>10}")
    print("="*50 + "\n")

    target_conn.close()


# =========================================================
def source_database(source_conn,source_cur):
    print("\n" + "="*50)
    print("         SOURCE DATABASE SUMMARY")
    print("="*50)

    source_cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    source_table = [i[0] for i in source_cur.fetchall()]

    print(f"\nTotal Tables: {len(source_table)}")
    print("-"*50)

    # Table header
    print(f"{'TABLE NAME':<25} | {'ROWS':>10}")
    print("-"*50)

    total_rows = 0

    # Loop tables
    for table in source_table:
        source_cur.execute(f"SELECT COUNT(*) FROM {table}")
        count = source_cur.fetchone()[0]
        total_rows += count

        print(f"{table:<25} | {count:>10}")

    print("-"*50)
    print(f"{'TOTAL':<25} | {total_rows:>10}")
    print("="*50 + "\n")


    source_conn.commit()
    source_conn.close()



choice = input("Select option:\n1) Source Database\n2) Target Database\nEnter choice (1 or 2): ")

if choice == "1":
    source_database(source_conn,source_cur)

elif choice == "2":
    target_database(target_conn,target_cur)

else:
    print("❌ Invalid choice! Please enter 1 or 2.")