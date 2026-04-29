import sqlite3, random

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

rows=c.execute("SELECT id,company FROM leads WHERE status='contacted'").fetchall()

for r in rows:
    if random.randint(1,10)==1:
        amount=random.choice([99000,149000,199000,249000])
        c.execute("INSERT INTO sales(company,amount) VALUES(?,?)",(r[1],amount))
        c.execute("UPDATE leads SET status='won' WHERE id=?",(r[0],))
        print("💰 WON:",r[1],amount,"FT")

db.commit()
db.close()
