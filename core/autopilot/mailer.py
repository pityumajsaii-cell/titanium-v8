import sqlite3, datetime

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

rows=c.execute("SELECT id,company,email FROM leads WHERE status='new' LIMIT 20").fetchall()

for r in rows:
    lid,company,email=r
    print("📨 OFFER SENT:",company,email)
    c.execute("UPDATE leads SET status='contacted' WHERE id=?",(lid,))

db.commit()
db.close()
