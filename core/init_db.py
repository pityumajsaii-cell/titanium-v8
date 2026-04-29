import sqlite3, os

os.makedirs("data", exist_ok=True)

db = sqlite3.connect("data/titanium.db")
c = db.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS leads(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
company TEXT,
service TEXT,
message TEXT,
status TEXT DEFAULT 'new',
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS sales(
id INTEGER PRIMARY KEY AUTOINCREMENT,
lead_id INTEGER,
company TEXT,
service TEXT,
amount INTEGER,
payment_method TEXT,
status TEXT DEFAULT 'pending',
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS services(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
category TEXT,
price INTEGER,
description TEXT
)
""")

db.commit()
db.close()
print("✅ LIVE DATABASE READY")
