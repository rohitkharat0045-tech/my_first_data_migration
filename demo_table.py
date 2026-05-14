import sqlite3
import random
from datetime import datetime, timedelta

# ============================================
# DATABASE CONNECTION
# ============================================

DB_PATH = "data/source.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("✅ Connected to database")

random.seed(42)

# ============================================
# SAMPLE DATA
# ============================================

first_names = ["Aarav", "Ishita", "Riya", "Kabir", "Neha", "Rahul", "Pooja", "Vikas", "Ananya", "Sahil"]

last_names = ["Patil", "Sharma", "Verma", "Gupta", "Singh", "Joshi", "Kumar", "Nair", "Mehta", "Yadav"]

cities = ["Pune", "Mumbai", "Delhi", "Bangalore", "Hyderabad"]

departments = ["HR", "IT", "Finance", "Marketing", "Sales"]

project_status = ["Pending", "Completed", "In Progress"]

attendance_status = ["Present", "Absent", "WFH", "Leave"]

leave_types = ["Sick Leave", "Casual Leave", "Paid Leave"]

asset_types = ["Laptop", "Monitor", "Phone", "Printer"]

actions = ["LOGIN", "LOGOUT", "UPDATE", "DELETE", "INSERT"]

# ============================================
# RANDOM DATE FUNCTION
# ============================================

def random_date(days=365):
    date = datetime.now() - timedelta(days=random.randint(0, days))
    return date.strftime("%Y-%m-%d")

# ============================================
# DEPARTMENTS TABLE
# ============================================

department_rows = []

for i in range(1, 6):

    department_rows.append((
        i,
        departments[i - 1],
        random.choice(cities),
        round(random.uniform(500000, 2000000), 2)
    ))

cursor.executemany("""
INSERT INTO departments (
    dept_id,
    dept_name,
    location,
    budget
)
VALUES (?, ?, ?, ?)
""", department_rows)

conn.commit()

print("✅ Departments Inserted")

# ============================================
# EMPLOYEES TABLE
# ============================================

employee_rows = []

for i in range(1, 100001):

    first = random.choice(first_names)
    last = random.choice(last_names)

    employee_rows.append((
        i,
        first,
        last,
        f"{first.lower()}.{last.lower()}{i}@company.com",
        f"98765{random.randint(10000,99999)}",
        random_date(1500),
        round(random.uniform(25000, 150000), 2),
        random.randint(1, 5)
    ))

cursor.executemany("""
INSERT INTO employees (
    emp_id,
    first_name,
    last_name,
    email,
    phone,
    hire_date,
    salary,
    dept_id
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", employee_rows)

conn.commit()

print("✅ Employees Inserted")

# ============================================
# PROJECTS TABLE
# ============================================

project_rows = []

for i in range(1, 5001):

    project_rows.append((
        i,
        f"Project_{i}",
        random_date(700),
        random_date(100),
        round(random.uniform(50000, 1000000), 2),
        random.randint(1, 5)
    ))

cursor.executemany("""
INSERT INTO projects (
    project_id,
    project_name,
    start_date,
    end_date,
    budget,
    dept_id
)
VALUES (?, ?, ?, ?, ?, ?)
""", project_rows)

conn.commit()

print("✅ Projects Inserted")

# ============================================
# TASKS TABLE
# ============================================

task_rows = []

for i in range(1, 20001):

    task_rows.append((
        i,
        f"Task_{i}",
        random.choice(project_status),
        random_date(60),
        random.randint(1, 100000),
        random.randint(1, 5000)
    ))

cursor.executemany("""
INSERT INTO tasks (
    task_id,
    task_name,
    status,
    deadline,
    emp_id,
    project_id
)
VALUES (?, ?, ?, ?, ?, ?)
""", task_rows)

conn.commit()

print("✅ Tasks Inserted")

# ============================================
# SALARIES TABLE
# ============================================

salary_rows = []

for i in range(1, 50001):

    salary_rows.append((
        i,
        random.randint(1, 100000),
        round(random.uniform(25000, 100000), 2),
        round(random.uniform(1000, 15000), 2),
        round(random.uniform(500, 5000), 2),
        random_date(365)
    ))

cursor.executemany("""
INSERT INTO salaries (
    salary_id,
    emp_id,
    basic_salary,
    bonus,
    deductions,
    payment_date
)
VALUES (?, ?, ?, ?, ?, ?)
""", salary_rows)

conn.commit()

print("✅ Salaries Inserted")

# ============================================
# ATTENDANCE TABLE
# ============================================

attendance_rows = []

for i in range(1, 50001):

    attendance_rows.append((
        i,
        random.randint(1, 100000),
        random_date(365),
        random.choice(attendance_status),
        "09:00",
        "18:00"
    ))

cursor.executemany("""
INSERT INTO attendance (
    attendance_id,
    emp_id,
    attendance_date,
    status,
    check_in,
    check_out
)
VALUES (?, ?, ?, ?, ?, ?)
""", attendance_rows)

conn.commit()

print("✅ Attendance Inserted")

# ============================================
# LEAVES TABLE
# ============================================

leave_rows = []

for i in range(1, 10001):

    leave_rows.append((
        i,
        random.randint(1, 100000),
        random.choice(leave_types),
        random_date(365),
        random_date(300),
        "Personal Reason"
    ))

cursor.executemany("""
INSERT INTO leaves (
    leave_id,
    emp_id,
    leave_type,
    start_date,
    end_date,
    reason
)
VALUES (?, ?, ?, ?, ?, ?)
""", leave_rows)

conn.commit()

print("✅ Leaves Inserted")

# ============================================
# CLIENTS TABLE
# ============================================

client_rows = []

for i in range(1, 5001):

    client_rows.append((
        i,
        f"Client_{i}",
        random.choice(first_names),
        f"client{i}@mail.com",
        f"98765{random.randint(10000,99999)}",
        random.choice(cities)
    ))

cursor.executemany("""
INSERT INTO clients (
    client_id,
    client_name,
    contact_person,
    email,
    phone,
    address
)
VALUES (?, ?, ?, ?, ?, ?)
""", client_rows)

conn.commit()

print("✅ Clients Inserted")

# ============================================
# MEETINGS TABLE
# ============================================

meeting_rows = []

for i in range(1, 10001):

    meeting_rows.append((
        i,
        f"Meeting_{i}",
        random_date(365),
        random.choice(cities),
        random.randint(1, 100000)
    ))

cursor.executemany("""
INSERT INTO meetings (
    meeting_id,
    meeting_title,
    meeting_date,
    location,
    organizer_id
)
VALUES (?, ?, ?, ?, ?)
""", meeting_rows)

conn.commit()

print("✅ Meetings Inserted")

# ============================================
# ASSETS TABLE
# ============================================

asset_rows = []

for i in range(1, 10001):

    asset_rows.append((
        i,
        f"Asset_{i}",
        random.choice(asset_types),
        random_date(2000),
        round(random.uniform(5000, 150000), 2),
        random.randint(1, 100000)
    ))

cursor.executemany("""
INSERT INTO assets (
    asset_id,
    asset_name,
    asset_type,
    purchase_date,
    asset_value,
    assigned_to
)
VALUES (?, ?, ?, ?, ?, ?)
""", asset_rows)

conn.commit()

print("✅ Assets Inserted")

# ============================================
# TRAINING TABLE
# ============================================

training_rows = []

for i in range(1, 10001):

    training_rows.append((
        i,
        f"Training_{i}",
        random.choice(first_names),
        random_date(365),
        random_date(300),
        random.randint(1, 100000)
    ))

cursor.executemany("""
INSERT INTO training (
    training_id,
    training_name,
    trainer_name,
    start_date,
    end_date,
    emp_id
)
VALUES (?, ?, ?, ?, ?, ?)
""", training_rows)

conn.commit()

print("✅ Training Inserted")

# ============================================
# AUDIT LOGS TABLE
# ============================================

audit_rows = []

for i in range(1, 50001):

    audit_rows.append((
        i,
        random.choice(first_names).lower(),
        random.choice(actions),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        f"Performed {random.choice(actions)} operation"
    ))

cursor.executemany("""
INSERT INTO audit_logs (
    log_id,
    user_name,
    action,
    log_time,
    description
)
VALUES (?, ?, ?, ?, ?)
""", audit_rows)

conn.commit()

print("✅ Audit Logs Inserted")

# ============================================
# DONE
# ============================================

print("\n🎉 All Tables Populated Successfully!")

conn.close()