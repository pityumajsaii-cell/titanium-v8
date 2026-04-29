import sqlite3, os, random

os.makedirs("data", exist_ok=True)

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

samples=[
("Tolna Digital Kft","info@tolnadigital.hu","+36301111111","Marketing","Tolna"),
("Szekszard Dental","info@szdent.hu","+36302222222","Dental","Szekszard"),
("Paks Bookkeeping","info@paksbook.hu","+36303333333","Accounting","Paks"),
("Budapest Media Pro","info@bmp.hu","+36304444444","Agency","Budapest")
]

for s in samples:
    try:
        c.execute("INSERT INTO leads(company,email,phone,industry,city,status) VALUES(?,?,?,?,?,'new')",s)
    except:
        pass

db.commit()
db.close()

print("🔎 AUTOPILOT LEADS IMPORTED")
