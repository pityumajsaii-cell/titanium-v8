import sqlite3

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS leads(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
company TEXT,
service TEXT,
status TEXT DEFAULT 'new',
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS crm(
id INTEGER PRIMARY KEY AUTOINCREMENT,
lead_id INTEGER,
note TEXT,
stage TEXT,
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS revenue(
id INTEGER PRIMARY KEY AUTOINCREMENT,
client TEXT,
amount INTEGER,
source TEXT,
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

db.commit()
db.close()

print("✅ V4 DATABASE READY")
