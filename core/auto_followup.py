import sqlite3

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

rows=c.execute("""
SELECT id,name,email,company FROM leads
WHERE status='new'
LIMIT 50
""").fetchall()

count=0

for r in rows:
    lead_id=r[0]
    msg=f"Hello {r[1]}, thanks for your interest. We can help {r[3]} grow with AI systems."

    c.execute("INSERT INTO followups(lead_id,message) VALUES(?,?)",(lead_id,msg))
    c.execute("UPDATE leads SET status='contacted' WHERE id=?", (lead_id,))
    count+=1

db.commit()
db.close()

print(f"📨 FOLLOWUPS CREATED: {count}")
