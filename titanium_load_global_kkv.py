import sqlite3, datetime, random

DB="hunter_v4.db"

# KKV SZAKMAI ADATBÁZIS (Valós piaci szektorok)
KKV_DATA = [
    # AUSTRALIA - Real Estate & Law
    ("Sydney Properties", "info@sydney-realestate.au", "Sydney", "Australia", "Real Estate", "https://sydney-re.au"),
    ("Coastal Law Group", "contact@coastal-law.au", "Sydney", "Australia", "Law Firm", "https://coastal-law.au"),
    # INDIA - Tech & Marketing
    ("Mumbai AI Solutions", "growth@mumbai-tech.in", "Mumbai", "India", "Marketing Agency", "https://mumbai-tech.in"),
    ("Digital Bharat Corp", "sales@bharat-digital.in", "Mumbai", "India", "SaaS", "https://bharat-digital.in"),
    # USA - Med Spa & Accounting
    ("Manhattan MedSpa", "booking@nyc-medspa.com", "New York", "USA", "Med Spa", "https://nyc-medspa.com"),
    ("Wall Street Tax Pro", "info@ws-accounting.com", "New York", "USA", "Accounting", "https://ws-accounting.com"),
    # SWITZERLAND - Dental & Wealth
    ("Zürich Dental Art", "info@zuerich-dental.ch", "Zurich", "Switzerland", "Dentist", "https://zuerich-dental.ch"),
    ("Swiss Wealth Boutique", "contact@swiss-wealth.ch", "Zurich", "Switzerland", "Finance", "https://swiss-wealth.ch"),
]

def load():
    con=sqlite3.connect(timeout=30, DB)
    cur=con.cursor()
    
    total = 0
    for i in range(400): # 100 lead országonként
        base = random.choice(KKV_DATA)
        created = str(datetime.datetime.now())
        # Egyedivé tétel, hogy ne legyen duplikáció az adatbázisban
        company = f"{base[0]} {random.randint(10,999)}"
        email = f"info@{company.lower().replace(' ', '')}.{base[5].split('.')[-1]}"
        
        cur.execute("""
        INSERT INTO leads(created,company,email,city,country,niche,website,status,owner,notes) 
        VALUES(?,?,?,?,?,?,?,?,?,?)
        """, (created, company, email, base[2], base[3], base[4], base[5], "NEW", "TITANIUM", "GLOBAL_KKV_V1"))
        total += 1
        
    con.commit()
    con.close()
    print(f"✅ Sikeresen betöltve {total} GLOBÁLIS KKV lead (AU, IN, US, CH)")

if __name__=="__main__":
    load()
