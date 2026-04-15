import csv
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path("sample_data")
BASE_DIR.mkdir(exist_ok=True)

random.seed(42)

first_names = ["Aarav", "Ishita", "Riya", "Kabir", "Neha", "Rahul", "Pooja", "Vikas", "Ananya", "Sahil"]
last_names = ["Patil", "Sharma", "Verma", "Gupta", "Singh", "Joshi", "Kumar", "Nair", "Mehta", "Yadav"]
cities = ["Pune", "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Nagpur", "Surat"]
states = ["MH", "MH", "DL", "KA", "TS", "TN", "MH", "GJ"]
tiers = ["bronze", "silver", "gold", "platinum"]
categories = ["Electronics", "Fashion", "Home", "Books", "Grocery"]
brands = ["Apex", "Nova", "Orbit", "Zen", "Prime"]
channels = ["web", "mobile", "store"]
statuses = ["placed", "shipped", "delivered", "cancelled", "returned"]
payment_methods = ["upi", "card", "netbanking", "wallet", "cod"]
payment_statuses = ["success", "failed", "pending"]
return_reasons = ["damaged", "wrong_item", "late_delivery", "changed_mind"]
coupon_codes = ["NEW10", "SAVE20", "FESTIVE5", "", "", ""]

def rand_date(start_days_ago=365):
    days_back = random.randint(0, start_days_ago)
    dt = datetime.now() - timedelta(days=days_back, hours=random.randint(0, 23), minutes=random.randint(0, 59))
    return dt

def write_csv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

def generate_customers(n=1000):
    rows = []
    for i in range(1, n + 1):
        fn = random.choice(first_names)
        ln = random.choice(last_names)
        city = random.choice(cities)
        idx = cities.index(city)
        state = states[idx]
        signup = rand_date(900).strftime("%Y-%m-%d")
        tier = random.choice(tiers)
        email = f"{fn.lower()}.{ln.lower()}{i}@mail.com"
        if random.random() < 0.02:
            email = ""  # bad/missing email
        rows.append([i, f"{fn} {ln}", email, city, state, signup, tier])
    write_csv(BASE_DIR / "customers.csv",
              ["customer_id", "customer_name", "email", "city", "state", "signup_date", "tier"],
              rows)

def generate_products(n=300):
    rows = []
    for i in range(1, n + 1):
        category = random.choice(categories)
        brand = random.choice(brands)
        price = round(random.uniform(100, 50000), 2)
        rows.append([i, f"{brand}-{category[:3]}-{i}", category, brand, price])
    write_csv(BASE_DIR / "products.csv",
              ["product_id", "product_name", "category", "brand", "price"],
              rows)

def generate_orders(n=10000, customer_count=1000):
    rows = []
    for i in range(1, n + 1):
        cid = random.randint(1, customer_count)
        od = rand_date(365).strftime("%Y-%m-%d %H:%M:%S")
        status = random.choices(statuses, weights=[40, 25, 20, 10, 5])[0]
        channel = random.choice(channels)
        coupon = random.choice(coupon_codes)
        total = round(random.uniform(200, 20000), 2)
        if random.random() < 0.01:
            total = -total  # bad value
        rows.append([i, cid, od, status, channel, coupon, total])
    write_csv(BASE_DIR / "orders.csv",
              ["order_id", "customer_id", "order_date", "order_status", "channel", "coupon_code", "order_total"],
              rows)

def generate_order_items(n=30000, order_count=10000, product_count=300):
    rows = []
    for i in range(1, n + 1):
        oid = random.randint(1, order_count)
        pid = random.randint(1, product_count)
        qty = random.randint(1, 5)
        unit_price = round(random.uniform(100, 50000), 2)
        rows.append([i, oid, pid, qty, unit_price, round(qty * unit_price, 2)])
    write_csv(BASE_DIR / "order_items.csv",
              ["order_item_id", "order_id", "product_id", "quantity", "unit_price", "line_amount"],
              rows)

def generate_payments(n=12000, order_count=10000):
    rows = []
    for i in range(1, n + 1):
        oid = random.randint(1, order_count)
        method = random.choice(payment_methods)
        status = random.choices(payment_statuses, weights=[80, 10, 10])[0]
        amount = round(random.uniform(200, 20000), 2)
        if random.random() < 0.02:
            amount = amount + random.uniform(1, 100)  # mismatch
        pt = rand_date(365).strftime("%Y-%m-%d %H:%M:%S")
        rows.append([i, oid, method, status, amount, pt])
    write_csv(BASE_DIR / "payments.csv",
              ["payment_id", "order_id", "payment_method", "payment_status", "paid_amount", "payment_time"],
              rows)

def generate_returns(n=500, order_count=10000):
    rows = []
    for i in range(1, n + 1):
        oid = random.randint(1, order_count)
        reason = random.choice(return_reasons)
        rdate = rand_date(365).strftime("%Y-%m-%d")
        refund = round(random.uniform(100, 10000), 2)
        rows.append([i, oid, reason, rdate, refund])
    write_csv(BASE_DIR / "returns.csv",
              ["return_id", "order_id", "reason", "return_date", "refund_amount"],
              rows)

def generate_bad_orders():
    rows = [
        ["101", "1", "2026-01-10 10:10:10", "placed", "web", "", "1200.50"],
        ["102", "", "2026-01-10 11:10:10", "delivered", "mobile", "SAVE20", "ABC"],   # bad customer_id and amount
        ["103", "3", "", "shipped", "store", "", "500"],                              # missing date
        ["104", "4", "2026-01-10 13:10:10", "", "web", "", "700"],                   # missing status
    ]
    write_csv(BASE_DIR / "bad_orders.csv",
              ["order_id", "customer_id", "order_date", "order_status", "channel", "coupon_code", "order_total"],
              rows)

def generate_web_events(n=5000, customer_count=1000):
    events = []
    for i in range(1, n + 1):
        customer_id = random.randint(1, customer_count)
        session_id = f"sess_{random.randint(100000, 999999)}"
        event_time = rand_date(30).isoformat()
        event_type = random.choice(["page_view", "search", "add_to_cart", "checkout", "purchase"])
        event_count = random.randint(1, 5)
        nested_events = []
        for j in range(event_count):
            nested_events.append({
                "event_id": f"e{i}_{j}",
                "event_type": random.choice(["click", "scroll", "view", "hover"]),
                "page": random.choice(["home", "product", "cart", "payment", "search"]),
                "duration_sec": random.randint(1, 300)
            })
        events.append({
            "session_id": session_id,
            "customer_id": customer_id,
            "event_time": event_time,
            "event_type": event_type,
            "events": nested_events
        })
    with open(BASE_DIR / "web_events.json", "w", encoding="utf-8") as f:
        for row in events:
            f.write(json.dumps(row) + "\n")

generate_customers(1000)
generate_products(300)
generate_orders(10000, 1000)
generate_order_items(30000, 10000, 300)
generate_payments(12000, 10000)
generate_returns(500, 10000)
generate_bad_orders()
generate_web_events(5000, 1000)

print(f"Sample data created in: {BASE_DIR.resolve()}")