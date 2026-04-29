import sqlite3,sys

if len(sys.argv)<3:
    print('HASZNALAT:')
    print('python3 core/close.py "Ceg" 199000')
    exit()

company=sys.argv[1]
amount=int(sys.argv[2])

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

c.execute("INSERT INTO sales(company,amount) VALUES(?,?)",(company,amount))
c.execute("UPDATE leads SET status='won' WHERE company=?",(company,))

db.commit()
db.close()

print("💰 DEAL LEZARVA:",company,amount,"FT")
