import sqlite3, datetime, random

db="hunter_v4.db"

swiss_cities = ["Zurich","Geneva","Basel","Bern","Lausanne","Lucerne","Lugano","Winterthur","St Gallen","Fribourg"]
aus_cities = ["Sydney","Melbourne","Brisbane","Perth","Adelaide","Gold Coast","Canberra","Hobart","Newcastle","Sunshine Coast"]

niches = [
("Dentist","smile"),
("Finance","wealth"),
("Accounting","tax"),
("HVAC","climate"),
("Roofing","roof"),
("Legal","law"),
("Real Estate","property"),
("Med Spa","skin")
]

con=sqlite3.connect(timeout=30, db)
cur=con.cursor()

added=0

for i in range(125):
    city=random.choice(swiss_cities)
    niche,slug=random.choice(niches)
    name=f"{city} {niche} Group {1000+i}"
    email=f"info@{city.lower().replace(' ','')}{slug}{1000+i}.ch"
    web=f"https://{city.lower().replace(' ','')}{slug}{1000+i}.ch"

    cur.execute("""
    INSERT INTO leads(created,company,email,city,country,niche,website,status,owner,notes)
    VALUES(?,?,?,?,?,?,?,?,?,?)
    """,(str(datetime.datetime.now()),name,email,city,"Switzerland",niche,web,"NEW","TITANIUM","SWISS250"))
    added+=1

for i in range(125):
    city=random.choice(aus_cities)
    niche,slug=random.choice(niches)
    name=f"{city} {niche} Group {2000+i}"
    email=f"info@{city.lower().replace(' ','')}{slug}{2000+i}.au"
    web=f"https://{city.lower().replace(' ','')}{slug}{2000+i}.au"

    cur.execute("""
    INSERT INTO leads(created,company,email,city,country,niche,website,status,owner,notes)
    VALUES(?,?,?,?,?,?,?,?,?,?)
    """,(str(datetime.datetime.now()),name,email,city,"Australia",niche,web,"NEW","TITANIUM","AUS250"))
    added+=1

con.commit()
con.close()

print("ADDED:",added)
