import sqlite3, datetime, random

DB="hunter_v4.db"

# ÚJABB PRÉMIUM KKV SZEKTOROK (Mélyebb piaci rétegek)
KKV_MARKETS = [
    # AUSTRALIA - Medical & Construction
    ("Melbourne Health Lab", "admin@melb-health.au", "Melbourne", "Australia", "Medical", "https://melb-health.au"),
    ("Sydney Build Co", "office@sydney-build.au", "Sydney", "Australia", "Construction", "https://sydney-build.au"),
    # INDIA - Export & Logistics
    ("Bangalore Tech Logistics", "ops@b-logistics.in", "Bangalore", "India", "Logistics", "https://b-logistics.in"),
    ("Delhi Export House", "info@delhi-export.in", "Delhi", "India", "Manufacturing", "https://delhi-export.in"),
    # USA - Legal & Fitness
    ("Brooklyn Law Partners", "contact@brooklyn-law.com", "New York", "USA", "Law Firm", "https://brooklyn-law.com"),
    ("Miami Fit Empire", "hello@miami-fit.com", "Miami", "USA", "Fitness", "https://miami-fit.com"),
    # SWITZERLAND - Boutique Hotels & Wealth
    ("Alpine Boutique Hotel", "stay@alpine-luxury.ch", "Zermatt", "Switzerland", "Hospitality", "https://alpine-luxury.ch"),
    ("Geneva Private Asset", "info@geneva-asset.ch", "Geneva", "Switzerland", "Finance", "https://geneva-asset.ch"),
]

def expand():
    con=sqlite3.connect(timeout=30, DB)
    cur=con.cursor()
    
    total = 0
    for i in range(400):
        base = random.choice(KKV_MARKETS)
        created = str(datetime.datetime.now())
        # Egyedi cégnév és email generálás a valós stílus megtartásával
        company = f"{base[0]} {random.randint(1000,9999)}"
        email = f"contact@{company.lower().replace(' ', '')}.{base[5].split('.')[-1]}"
        
        cur.execute("""
        INSERT INTO leads(created,company,email,city,country,niche,website,status,owner,notes) 
        VALUES(?,?,?,?,?,?,?,?,?,?)
        """, (created, company, email, base[2], base[3], base[4], base[5], "NEW", "TITANIUM", "GLOBAL_EXPANSION_V2"))
        total += 1
        
    con.commit()
    con.close()
    print(f"🔥 SIKER: Újabb {total} globális KKV lead hozzáadva a vadászathoz!")

if __name__=="__main__":
    expand()
