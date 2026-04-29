import sqlite3, random

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

rows=c.execute("""
SELECT id,name,company,service FROM leads
WHERE status='new'
LIMIT 50
""").fetchall()

count=0

for r in rows:
    lid,name,company,service=r

    note=f"Auto contacted {company} for {service}"

    c.execute("""
    INSERT INTO crm(lead_id,note,stage)
    VALUES(?,?,?)
    """,(lid,note,"contacted"))

    c.execute("UPDATE leads SET status='contacted' WHERE id=?", (lid,))
    count+=1

db.commit()
db.close()

print(f"📨 FOLLOWUPS DONE: {count}")
