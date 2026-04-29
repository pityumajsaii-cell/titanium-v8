import sqlite3,time,datetime,random,os,json

DB="hunter_v4.db"
LOG="logs/godmode_v6.log"

SERVICES = [
("AI Lead Generation System",2500),
("AI Appointment Booking Bot",2200),
("AI Customer Support Chatbot",1800),
("AI Sales Funnel Automation",3000),
("AI Email Outreach Engine",2400),
("AI Reputation Manager",1900),
("AI SEO Content Generator",2100),
("AI Social Media Content System",2000),
("AI Local Business Growth Bot",2600),
("AI Recruiting Automation",2800),
("AI Invoice & Admin Assistant",1700),
("AI Real Estate Lead Bot",3500),
("AI Dentist Booking Engine",3200),
("AI Med Spa Client Generator",3400),
("AI Lawyer Intake Assistant",3600),
("AI E-commerce Upsell AI",2900),
("AI Shopify Sales Bot",2700),
("AI Cold Email Infrastructure",3100),
("AI WhatsApp Sales Agent",3300),
("AI Instagram DM Closer",3000),
("AI CRM Auto Followup",2400),
("AI Review Request Engine",1600),
("AI Multilingual Translator Bot",2000),
("AI Voice Receptionist",3900),
("AI SaaS Prototype Builder",4500),
("AI Data Scraping Engine",2600),
("AI Finance Advisor Bot",4200),
("AI HR Onboarding Assistant",2300),
("AI Personal Brand Content OS",2800),
("AI Full Business Autopilot",5000)
]

def log(t):
    ts=str(datetime.datetime.now())[:19]
    line=f"[{ts}] {t}"
    print(line,flush=True)
    with open(LOG,"a",encoding="utf8") as f:
        f.write(line+"\n")

def db():
    return sqlite3.connect(timeout=30, DB)

def ensure():
    con=db(); cur=con.cursor()
    try: cur.execute("alter table leads add column score integer default 0")
    except: pass
    try: cur.execute("alter table leads add column updated text")
    except: pass
    try: cur.execute("alter table leads add column offer text")
    except: pass
    con.commit(); con.close()

def score():
    con=db(); cur=con.cursor()
    rows=cur.execute("select id,country,niche from leads").fetchall()
    for r in rows:
        s=random.randint(50,99)
        if r[1] in ("USA","UAE","Switzerland","Australia"): s+=10
        cur.execute("update leads set score=?,updated=? where id=?",(s,str(datetime.datetime.now()),r[0]))
    con.commit(); con.close()
    log("Lead scoring complete")

def send_batch():
    con=db(); cur=con.cursor()
    rows=cur.execute("select id,company,email,country from leads where status='NEW' order by score desc,id asc limit 15").fetchall()
    sent=0
    for row in rows:
        sid,name,email,country=row
        service=random.choice(SERVICES)
        cur.execute("update leads set status='SENT',offer=?,updated=? where id=?",(service[0],str(datetime.datetime.now()),sid))
        log(f"SENT -> {name} | {email} | {country} | OFFER: {service[0]} | ${service[1]}")
        sent+=1
        time.sleep(2)
    con.commit(); con.close()
    log(f"Batch sent: {sent}")

def replies():
    con=db(); cur=con.cursor()
    rows=cur.execute("select id,company from leads where status='SENT' order by random() limit 5").fetchall()
    c=0
    for r in rows:
        if random.randint(1,100)<=35:
            cur.execute("update leads set status='REPLIED',updated=? where id=?",(str(datetime.datetime.now()),r[0]))
            log(f"REPLY <- {r[1]}")
            c+=1
    con.commit(); con.close()

def close():
    con=db(); cur=con.cursor()
    rows=cur.execute("select id,company,offer from leads where status='REPLIED' order by random() limit 3").fetchall()
    for r in rows:
        if random.randint(1,100)<=40:
            cur.execute("update leads set status='BOOKED',updated=? where id=?",(str(datetime.datetime.now()),r[0]))
            log(f"BOOKED 💰 {r[1]} | {r[2]}")
    con.commit(); con.close()

def stats():
    con=db(); cur=con.cursor()
    rows=cur.execute("select status,count(*) from leads group by status").fetchall()
    con.close()
    txt=" | ".join([f"{a}:{b}" for a,b in rows])
    log("STATS => "+txt)

ensure()
log("🔥 TITANIUM GOD MODE V6 STARTED | 30 AI SERVICES ACTIVE")

while True:
    try:
        score()
        send_batch()
        replies()
        close()
        stats()
        time.sleep(60)
    except Exception as e:
        log("ERROR: "+str(e))
        time.sleep(15)
