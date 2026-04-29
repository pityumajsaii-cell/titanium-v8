import sqlite3, csv, datetime, requests, re, time
from urllib.parse import quote_plus

DB="real_money.db"
CSV="real_leads.csv"

TARGETS = [
    ("Dubai","UAE"),
    ("New York","USA"),
    ("Mumbai","India"),
    ("Sydney","Australia"),
    ("Zurich","Switzerland"),
    ("London","UK")
]

KEYWORDS = [
    "dentist",
    "law firm",
    "real estate",
    "med spa",
    "accounting",
    "ecommerce agency"
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
        niche TEXT,
        city TEXT,
        country TEXT,
        source TEXT,
        status TEXT,
        notes TEXT
    )
    """)
    con.commit()
    con.close()

def save(row):
    con=sqlite3.connect(timeout=30, DB)
    cur=con.cursor()
    cur.execute("""
    INSERT INTO leads(created,company,email,niche,city,country,source,status,notes)
    VALUES(?,?,?,?,?,?,?,?,?)
    """,row)
    con.commit()
    con.close()

    with open(CSV,"a",newline="",encoding="utf-8") as f:
        csv.writer(f).writerow(row)

def find_emails(text):
    return list(set(re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)))

def scrape(query, city, country):
    url="https://duckduckgo.com/html/?q="+quote_plus(query+" "+city)
    try:
        r=requests.get(url,timeout=10,headers={"User-Agent":"Mozilla/5.0"})
        text=r.text
        emails=find_emails(text)
        return emails[:3]
    except:
        return []

def run():
    init()
    total=0

    for city,country in TARGETS:
        print(f"🌍 {city}, {country}")

        for niche in KEYWORDS:
            print("🔎", niche)

            emails=scrape(niche,city,country)

            for e in emails:
                company=e.split("@")[1].split(".")[0].title()

                row=(
                    str(datetime.datetime.now()),
                    company,
                    e,
                    niche,
                    city,
                    country,
                    "DuckDuckGo",
                    "NEW",
                    "Needs outreach"
                )

                save(row)
                total+=1
                print("✅",company,e)

            time.sleep(2)

    print("")
    print("================================")
    print("💰 REAL MONEY V3 COMPLETE")
    print("📦 LEADS:",total)
    print("📁 CSV:",CSV)
    print("🗄 DB :",DB)
    print("================================")

if __name__=="__main__":
    run()
