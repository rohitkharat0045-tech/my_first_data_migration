# 🚀 Automated Database Migration Tool

## 📌 Overview

This project is a Python-based automated database migration tool that transfers data from a source database (SQLite) to a target database (SQLite/PostgreSQL). It follows the ETL (Extract, Transform, Load) pipeline and includes logging, error handling, and report generation.

---

## 🎯 Features

* 🔄 Automated data migration
* 🧩 Schema extraction and transformation
* 🗄️ Supports SQLite (and extendable to PostgreSQL)
* 📝 Logging system for tracking execution
* 📊 Report generation after migration
* ⚠️ Error handling for robustness

---

## 🛠️ Tech Stack

* Python
* SQLite
* (Optional) PostgreSQL
* python-dotenv

---

## 📁 Project Structure

```
db-migration-tool/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── migrate.py
│
├── config/
│   └── db_config.json
│
├── data/
│   └── source.db
│
├── logs/
├── reports/
│
├── .env
├── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/vikaslokhande2004/db-migration-tool.git
cd db-migration-tool
```

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate:

* Windows: `venv\Scripts\activate`
* Linux/Mac: `source venv/bin/activate`

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create `.env` file:

```
DB_HOST=localhost
DB_NAME=migration_db
DB_USER=postgres
DB_PASSWORD=your_password
```

---

### 5. Run Migration

```
cd src
python migrate.py
```

---

## 📊 Output

### ✅ Terminal

```
Migration Done! Rows: 2, Errors: 0
```

### 📄 Logs

Stored in:

```
logs/app.log
```

### 📑 Report

Stored in:

```
reports/report.txt
```

---

## 🧠 How It Works

1. **Extract** → Reads schema and data from source DB
2. **Transform** → Converts data types
3. **Load** → Creates table and inserts data into target DB

---

## 🚀 Future Enhancements

* Schema evolution detection
* Multi-database support
* Web dashboard for monitoring
* Large-scale data handling

---

## 👨‍💻 Author

Your Name

---

## ⭐ Acknowledgment

This project was developed as a final year academic project demonstrating ETL pipeline and database migration concepts.
