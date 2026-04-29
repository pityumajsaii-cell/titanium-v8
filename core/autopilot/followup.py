import sqlite3

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

rows=c.execute("SELECT id,company FROM leads WHERE status='contacted'").fetchall()

for r in rows:
    print("↪ FOLLOWUP:",r[1])

db.close()
