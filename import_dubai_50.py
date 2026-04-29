import sqlite3, csv, datetime, os

OWNER="leadholdingzrt@gmail.com"
DB="harvest.db"
CSV_FILE="dubai_dentist_import.csv"

leads = [
("The Dental Studio","info@thedentalstudio.ae","Dubai","UAE","Dentist","https://thedentalstudio.ae"),
("Dr Joy Dental Clinics","info@drjoydentalclinic.com","Dubai","UAE","Dentist","https://drjoydentalclinic.com"),
("DentalZorg","contact@dentalzorg.com","Dubai","UAE","Dentist","https://dentalzorg.com"),
("MedDental Clinic DMCC","info@meddental.ae","Dubai","UAE","Dentist","https://meddental.ae"),
("Versailles Dental Clinic","info@versaillesdentalclinic.com","Dubai","UAE","Dentist","https://versaillesdentalclinic.com"),
("Tower Clinic","frontdesk@towerclinic.com","Dubai","UAE","Dentist","https://towerclinic.com"),
("My Dental Clinic","reception@mydentalclinic.ae","Dubai","UAE","Dentist","https://mydentalclinic.ae"),
]

con=sqlite3.connect(timeout=30, DB)
cur=con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS leads(
id INTEGER PRIMARY KEY AUTOINCREMENT,
created TEXT,
company TEXT,
email TEXT,
city TEXT,
country TEXT,
niche TEXT,
website TEXT,
status TEXT,
owner TEXT,
notes TEXT
)
""")

for row in leads:
    created=str(datetime.datetime.now())
    company,email,city,country,niche,website=row
    cur.execute("""
    INSERT INTO leads(created,company,email,city,country,niche,website,status,owner,notes)
    VALUES(?,?,?,?,?,?,?,?,?,?)
    """,(created,company,email,city,country,niche,website,"NEW",OWNER,"Dubai Dentist Import"))

with open(CSV_FILE,"w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["company","email","city","country","niche","website","status","owner"])
    for row in leads:
        company,email,city,country,niche,website=row
        w.writerow([company,email,city,country,niche,website,"NEW",OWNER])

con.commit()
con.close()

print("✅ Dubai dentist leads integrated")
print("📦 Added:", len(leads))
print("📁 CSV:", CSV_FILE)
print("👤 Owner:", OWNER)
