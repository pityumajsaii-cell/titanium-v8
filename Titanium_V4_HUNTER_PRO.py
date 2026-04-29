import requests, re, csv, sqlite3, datetime, time
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

DB="hunter_v4.db"
CSV="hunter_v4_leads.csv"

COUNTRIES = [
    ("Dubai","UAE"),
    ("New York","USA"),
    ("Zurich","Switzerland"),
    ("London","UK"),
    ("Sydney","Australia"),
    ("Mumbai","India")
]

NICHES = [
    "dentist",
    "law firm",
    "real estate",
    "med spa",
    "accounting",
    "marketing agency"
]

HEADERS={"User-Agent":"Mozilla/5.0"}

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
        status TEXT
    )
    """)
    con.commit()
    con.close()

def save(row):
    con=sqlite3.connect(timeout=30, DB)
    cur=con.cursor()
    cur.execute("""
    INSERT INTO leads(created,company,email,niche,city,country,source,status)
    VALUES(?,?,?,?,?,?,?,?)
    """,row)
    con.commit()
    con.close()

    with open(CSV,"a",newline="",encoding="utf-8") as f:
        csv.writer(f).writerow(row)

def emails(text):
    return list(set(re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)))

def search(query):
    try:
        url="https://duckduckgo.com/html/?q="+quote_plus(query)
        r=requests.get(url,headers=HEADERS,timeout=10)
        return r.text
    except:
        return ""

def extract_sites(html):
    soup=BeautifulSoup(html,"html.parser")
    links=[]
    for a in soup.find_all("a",href=True):
        h=a["href"]
        if "http" in h and "duckduckgo" not in h:
            links.append(h)
    return list(dict.fromkeys(links))[:5]

def scan_site(url):
    try:
        r=requests.get(url,headers=HEADERS,timeout=8)
        found=emails(r.text)
        return found[:2]
    except:
        return []

def run():
    init()
    total=0

    for city,country in COUNTRIES:
        print(f"🌍 {city}, {country}")

        for niche in NICHES:
            q=f"{niche} {city}"
            print("🔎",q)

            html=search(q)
            sites=extract_sites(html)

            for s in sites:
                found=scan_site(s)

                for e in found:
                    company=e.split("@")[1].split(".")[0].title()

                    row=(
                        str(datetime.datetime.now()),
                        company,
                        e,
                        niche,
                        city,
                        country,
                        s,
                        "NEW"
                    )

                    save(row)
                    total+=1
                    print("✅",company,e)

            time.sleep(2)

    print("")
    print("===================================")
    print("🚀 HUNTER PRO COMPLETE")
    print("📦 LEADS:",total)
    print("📁 CSV:",CSV)
    print("🗄 DB :",DB)
    print("===================================")

if __name__=="__main__":
    run()
