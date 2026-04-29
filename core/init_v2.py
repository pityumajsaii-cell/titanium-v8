import sqlite3

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS followups(
id INTEGER PRIMARY KEY AUTOINCREMENT,
lead_id INTEGER,
message TEXT,
sent INTEGER DEFAULT 0,
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

db.commit()
db.close()
print("✅ V2 DATABASE READY")
