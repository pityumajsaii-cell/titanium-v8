import csv, sqlite3, datetime, time, random
from pathlib import Path

DB = 'harvest.db'
CSV = 'harvest_leads.csv'
TARGETS = [('Dubai','UAE'), ('New York','USA'), ('Mumbai','India'), ('Sydney','Australia')]
NICHES = ['Dentist', 'Law Firm', 'Real Estate', 'Med Spa', 'Ecommerce', 'Accounting']

SAMPLE_DOMAINS = {
    'Dubai': ['example.ae'],
    'New York': ['example.com'],
    'Mumbai': ['example.in'],
    'Sydney': ['example.au']
}

def init():
    con = sqlite3.connect(timeout=30, DB)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS leads(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created TEXT,
        company TEXT,
        email TEXT,
        niche TEXT,
        city TEXT,
        country TEXT,
        status TEXT,
        notes TEXT)''')
    con.commit()
    con.close()

def gen_company(city, niche, i):
    return f'{city} {niche} Group {i}'

def gen_email(company, city):
    dom = SAMPLE_DOMAINS[city][0]
    local = company.lower().replace(' ', '').replace('&', '')[:18]
    return f'info@{local}.{dom.split(".")[-1]}'

def add_lead(row):
    con = sqlite3.connect(timeout=30, DB)
    cur = con.cursor()
    cur.execute('INSERT INTO leads(created,company,email,niche,city,country,status,notes) VALUES(?,?,?,?,?,?,?,?)', row)
    con.commit()
    con.close()
    with open(CSV, 'a', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(row)

def harvest(per_city=100):
    init()
    # CSV fejléc írása, ha még nincs
    if not Path(CSV).exists():
        with open(CSV, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(['Created','Company','Email','Niche','City','Country','Status','Notes'])

    for city, country in TARGETS:
        for i in range(1, per_city + 1):
            niche = random.choice(NICHES)
            company = gen_company(city, niche, i)
            email = gen_email(company, city)
            row = (str(datetime.datetime.now()), company, email, niche, city, country, 'NEW', 'Needs outreach')
            add_lead(row)
        print(f'✅ Loaded {per_city} leads for {city}')
    print('🚀 Harvest complete')

def make_offer(company, niche, city):
    return f'Hi {company}, we help {niche} businesses in {city} generate more booked appointments with AI automation.'

def outreach(limit=20):
    con = sqlite3.connect(timeout=30, DB)
    cur = con.cursor()
    cur.execute("SELECT id, company, email, niche, city FROM leads WHERE status='NEW' LIMIT ?", (limit,))
    rows = cur.fetchall()
    for r in rows:
        msg = make_offer(r[1], r[3], r[4])
        print(f'📧 {r[2]} => {msg}')
        cur.execute("UPDATE leads SET status='READY_TO_SEND' WHERE id=?", (r[0],))
    con.commit()
    con.close()
    print('🔥 Outreach queue prepared')

if __name__ == '__main__':
    harvest(100)
    outreach(40)
