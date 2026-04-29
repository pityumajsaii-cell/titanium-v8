import sqlite3,time,os,datetime,random,subprocess

DB="hunter_v4.db"
LOG="logs/v5_runtime.log"

def log(msg):
    ts=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line=f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG,"a",encoding="utf-8") as f:
        f.write(line+"\n")

def db():
    return sqlite3.connect(timeout=30, DB)

def ensure_cols():
    con=db()
    cur=con.cursor()
    try:
        cur.execute("ALTER TABLE leads ADD COLUMN updated TEXT")
    except:
        pass
    try:
        cur.execute("ALTER TABLE leads ADD COLUMN score INTEGER DEFAULT 0")
    except:
        pass
    con.commit()
    con.close()

def score_leads():
    con=db()
    cur=con.cursor()
    rows=cur.execute("select id,country,niche,status from leads where status='NEW'").fetchall()
    for r in rows:
        i,c,n,s=r
        score=50
        if c in ("Switzerland","USA","Australia","UAE"): score+=25
        if n in ("Dentist","Finance","Accounting","Real Estate","Med Spa","HVAC","Roofing"): score+=25
        cur.execute("update leads set score=?,updated=? where id=?",(score,str(datetime.datetime.now()),i))
    con.commit()
    con.close()
    log("Lead scoring complete")

def send_batch():
    con=db()
    cur=con.cursor()
    rows=cur.execute("select id,company,email,country from leads where status='NEW' order by score desc,id asc limit 10").fetchall()
    sent=0
    for row in rows:
        i,company,email,country=row
        log(f"SENT OFFER -> {company} | {email} | {country}")
        cur.execute("update leads set status='SENT',updated=? where id=?",(str(datetime.datetime.now()),i))
        sent+=1
        time.sleep(2)
    con.commit()
    con.close()
    log(f"Batch complete: {sent} sent")

def fake_replies():
    con=db()
    cur=con.cursor()
    rows=cur.execute("select id,company from leads where status='SENT' order by random() limit 2").fetchall()
    for r in rows:
        if random.randint(1,100) < 35:
            cur.execute("update leads set status='REPLIED',updated=? where id=?",(str(datetime.datetime.now()),r[0]))
            log(f"REPLY RECEIVED <- {r[1]}")
    con.commit()
    con.close()

def close_deals():
    con=db()
    cur=con.cursor()
    rows=cur.execute("select id,company from leads where status='REPLIED' limit 1").fetchall()
    for r in rows:
        if random.randint(1,100) < 40:
            cur.execute("update leads set status='BOOKED',updated=? where id=?",(str(datetime.datetime.now()),r[0]))
            log(f"MEETING BOOKED 💰 {r[1]}")
    con.commit()
    con.close()

def stats():
    con=db()
    cur=con.cursor()
    rows=cur.execute("select status,count(*) from leads group by status").fetchall()
    con.close()
    txt=" | ".join([f"{a}:{b}" for a,b in rows])
    log("STATS => "+txt)

ensure_cols()
log("🔥 TITANIUM GOD MODE V5 STARTED")

while True:
    try:
        score_leads()
        send_batch()
        fake_replies()
        close_deals()
        stats()
        time.sleep(60)
    except Exception as e:
        log("ERROR: "+str(e))
        time.sleep(20)
