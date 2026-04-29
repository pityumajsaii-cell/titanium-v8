import sqlite3,sys

if len(sys.argv)<6:
    print('HASZNALAT:')
    print('python3 core/lead_add.py "Ceg" "mail@x.hu" "+361..." "Industry" "City"')
    exit()

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

c.execute("INSERT INTO leads(company,email,phone,industry,city) VALUES(?,?,?,?,?)",
(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]))

db.commit()
db.close()

print("✅ LEAD HOZZAADVA")
