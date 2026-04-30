import sqlite3, smtplib, os
from email.mime.text import MIMEText
from datetime import datetime

DB="titanium_system.db"

def get_leads():
    con=sqlite3.connect(DB)
    cur=con.cursor()
    cur.execute("""
        SELECT id, company_name, email, location
        FROM leads
        WHERE status='new'
        AND email IS NOT NULL
        LIMIT 50
    """)
    return cur.fetchall()

def mark_sent(lead_id):
    con=sqlite3.connect(DB)
    cur=con.cursor()
    cur.execute("""
        UPDATE leads
        SET status='SENT',
            last_sent_engine='ENGINE_CORE_V1',
            sent_at=?
        WHERE id=?
    """,(datetime.now().isoformat(),lead_id))
    con.commit()

def send_email(to_email, company, location):
    user=os.getenv("GMAIL_USER")
    pw=os.getenv("GMAIL_PASS")

    msg=MIMEText(f"Hi {company}, offer for {location}")
    msg["Subject"]=f"Offer - {company}"
    msg["From"]=user
    msg["To"]=to_email

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as s:
        s.login(user,pw)
        s.send_message(msg)

def run():
    leads=get_leads()
    print("ENGINE CORE START:",len(leads))

    for id,co,em,loc in leads:
        try:
            send_email(em,co,loc)
            mark_sent(id)
            print("SENT:",co)
        except Exception as e:
            print("ERROR:",co,e)

if __name__=="__main__":
    run()
