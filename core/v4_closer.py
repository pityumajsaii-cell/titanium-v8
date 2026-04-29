import sqlite3, random

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

rows=c.execute("""
SELECT id,company,service FROM leads
WHERE status='contacted'
LIMIT 3
""").fetchall()

closed=0

for r in rows:
    lid,company,service=r
    amount=random.choice([299,499,699,999,1499])

    c.execute("""
    INSERT INTO revenue(client,amount,source)
    VALUES(?,?,?)
    """,(company,amount,service))

    c.execute("UPDATE leads SET status='won' WHERE id=?", (lid,))
    closed+=1

db.commit()
db.close()

print(f"💰 DEALS CLOSED: {closed}")
