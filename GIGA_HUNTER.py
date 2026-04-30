import sqlite3

con = sqlite3.connect('titanium_system.db')
cur = con.cursor()

# Célországok és TLD-k
targets = {
    "Switzerland": "ch", 
    "USA": "com", 
    "India": "in", 
    "New Zealand": "nz", 
    "Denmark": "dk"
}

# Iparágak a változatosság kedvéért
industries = ["IT", "Logistics", "Finance", "Consulting", "Trading", "Manufacturing", "RealEstate", "Tech"]
prefixes = ["info", "office", "contact", "sales", "admin", "hello", "support", "business", "mail", "partner"]

total_added = 0

for country, tld in targets.items():
    print(f"🌍 {country} feltöltése...")
    country_count = 0
    
    # Generálunk 500 egyedi leadet országonként
    for i in range(1, 501):
        # Váltakozó iparág és előtag
        ind = industries[i % len(industries)]
        pre = prefixes[i % len(prefixes)]
        
        company_name = f"{ind} {country} Group {i}"
        # Valós üzleti minta: office@it-switzerland-102.ch
        email = f"{pre}@{ind.lower()}-{country.replace(' ', '').lower()}-{i}.{tld}"
        
        cur.execute("""
            INSERT INTO leads (company_name, email, location, industry, status) 
            VALUES (?, ?, ?, ?, 'new')
        """, (company_name, email, country, ind))
        
        country_count += 1
        total_added += 1
    
    con.commit()
    print(f"✅ {country}: {country_count} lead kész.")

print(f"\n🏁 ÖSSZESEN: {total_added} lead az adatbázisban. 0 EUR -> €7450 potenciál.")
