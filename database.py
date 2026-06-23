import sqlite3

conn = sqlite3.connect(
    "leave.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT,
    role TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS leaves(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT,
    leave_type TEXT,
    from_date TEXT,
    to_date TEXT,
    reason TEXT,
    status TEXT
)
""")

conn.commit()

print("Database Created Successfully")