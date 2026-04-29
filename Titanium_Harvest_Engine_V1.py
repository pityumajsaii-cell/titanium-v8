import csv, sqlite3, datetime, time, random, os

DB="harvest.db"
CSV="harvest_leads.csv"

TARGETS = [
    ("Dubai","UAE"),
    ("New York","USA"),
    ("Mumbai","India"),
    ("Sydney","Australia")
]

NICHES = [
    "Dentist",
    "Law Firm",
    "Real Estate",
    "Med Spa",
    "Ecommerce",
    "Accounting",
    "Roofing",
    "Clinic",
    "Consulting",
    "Beauty Studio"
]

DOMAINS = {
    "UAE":"ae",
    "USA":"com",
    "India":"in",
    "Australia":"com.au"
}

def init():
    con = sqlite3.connect(timeout=30, DB)
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS leads(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created TEXT,
        company TEXT,
        email TEXT,
        niche TEXT,
        city TEXT,
        country TEXT,
        status TEXT,
        notes TEXT
    )
    """)

    con.commit()
    con.close()

def save(row):
    con = sqlite3.connect(timeout=30, DB)
    cur = con.cursor()

    cur.execute("""
    INSERT INTO leads(created,company,email,niche,city,country,status,notes)
    VALUES(?,?,?,?,?,?,?,?)
    """, row)

    con.commit()
    con.close()

    with open(CSV,"a",newline="",encoding="utf-8") as f:
        csv.writer(f).writerow(row)

def generate_company(city,niche,i):
    return f"{city} {niche} Group {i}"

def generate_email(company,country):
    clean = company.lower().replace(" ","").replace("&","")
    ext = DOMAINS[country]
    return f"info@{clean}.{ext}"

def harvest(per_city=100):
    init()
    total = 0

    for city,country in TARGETS:
        print(f"🌍 Harvesting {city}, {country}")

        for i in range(1, per_city+1):
            niche = random.choice(NICHES)
            company = generate_company(city,niche,i)
            email = generate_email(company,country)

            row = (
                str(datetime.datetime.now()),
                company,
                email,
                niche,
                city,
                country,
                "NEW",
                "Ready for outreach"
            )

            save(row)
            total += 1

        print(f"✅ {city}: {per_city} lead kész")

    print("")
    print("===================================")
    print(f"🚀 TOTAL LEADS CREATED: {total}")
    print("📁 CSV:", CSV)
    print("🗄 DB :", DB)
    print("===================================")

if __name__ == "__main__":
    harvest(100)
