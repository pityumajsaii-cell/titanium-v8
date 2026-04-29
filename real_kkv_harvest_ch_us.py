import sqlite3, requests, re, time, datetime
from urllib.parse import quote_plus

DB="hunter_v4.db"

TARGETS = [
    ("Zurich","Switzerland"),
    ("Geneva","Switzerland"),
    ("Basel","Switzerland"),
    ("New York","USA"),
    ("Miami","USA"),
    ("Los Angeles","USA")
]

KEYWORDS = [
    "dentist",
    "law firm",
    "accounting",
    "real estate",
    "marketing agency",
    "med spa"
]

def init():
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
    con.commit()
    con.close()

def emails(txt):
    return list(set(re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', txt)))

def domains(txt):
    return list(set(re.findall(r'https?://[^\s"]+', txt)))

def scrape(query):
    url="https://duckduckgo.com/html/?q="+quote_plus(query)
    try:
        r=requests.get(url,timeout=12,headers={"User-Agent":"Mozilla/5.0"})
        return r.text
    except:
        return ""

def save(company,email,city,country,niche,website):
    con=sqlite3.connect(timeout=30, DB)
    cur=con.cursor()
    cur.execute("""
    INSERT INTO leads(
    created,company,email,city,country,niche,website,status,owner,notes
    ) VALUES(?,?,?,?,?,?,?,?,?,?)
    """,(
    str(datetime.datetime.now()),
    company,email,city,country,niche,website,
    "NEW","TITANIUM","REAL_KKV_WEB"
    ))
    con.commit()
    con.close()

def run():
    init()
    total=0

    for city,country in TARGETS:
        print(f"\n🌍 {city}, {country}")

        for niche in KEYWORDS:
            q=f"{niche} {city} contact email"
            print("🔎",q)

            html=scrape(q)
            em=emails(html)[:5]
            dm=domains(html)[:5]

            for i,e in enumerate(em):
                company=e.split("@")[-1].split(".")[0].replace("-"," ").title()
                website=dm[i] if i < len(dm) else ""
                save(company,e,city,country,niche,website)
                total+=1
                print("✅",company,e)

            time.sleep(2)

    print("\n==========================")
    print("✅ REAL KKV HARVEST DONE")
    print("📦 Leads Added:",total)
    print("==========================")

if __name__=="__main__":
    run()
