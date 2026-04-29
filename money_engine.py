import sqlite3, smtplib, ssl, os, time
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL=os.getenv("EMAIL_USER")
PASS=os.getenv("EMAIL_PASS")

DB='titanium.db'

def send_mail(to_email, company):
    msg=MIMEText(f"""
Hi {company} team,

We help businesses generate more customers using AI automation, lead systems and conversion funnels.

Would you be open to a quick intro?

Best regards
Titanium Growth
""")

    msg["Subject"]="Quick growth idea for "+company
    msg["From"]=EMAIL
    msg["To"]=to_email

    ctx=ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ctx) as server:
        server.login(EMAIL,PASS)
        server.send_message(msg)

def run():
    con=sqlite3.connect(DB, timeout=60)
    try:
        con.execute("PRAGMA journal_mode=WAL")
    except:
        pass
    con.execute("PRAGMA busy_timeout=60000")
    cur=con.cursor()

    rows=cur.execute("""
    SELECT id,name,email
    FROM leads
    WHERE status='NEW'
    LIMIT 25
    """).fetchall()

    sent=0

    for row in rows:
        id_,company,email=row
        try:
            send_mail(email,company)
            cur.execute("UPDATE leads SET status='SENT' WHERE id=?",(id_,))
            con.commit()
            print("✅ SENT:",company,email)
            sent+=1
            time.sleep(4)
        except Exception as e:
            print("❌ FAIL:",email,e)

    print("🔥 DONE:",sent,"emails sent")

run()