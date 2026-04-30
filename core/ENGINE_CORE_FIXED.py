import sqlite3
import smtplib
import os
from email.mime.text import MIMEText
from datetime import datetime, timezone

DB = "titanium_system.db"
ENGINE_NAME = "ENGINE_CORE_V1"

def get_leads():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT id, company_name, email, location FROM leads WHERE status='new' AND email IS NOT NULL LIMIT 50")
    return cur.fetchall()

def mark_sent(conn, lead_id):
    cur = conn.cursor()
    cur.execute("""
        UPDATE leads
        SET status='SENT',
            last_sent_engine=?,
            sent_at=?
        WHERE id=?
    """, (ENGINE_NAME, datetime.now(timezone.utc).isoformat(), lead_id))
    conn.commit()

def send_email(to_email, company, location):
    user = os.getenv("USER_EMAIL")
    pw = os.getenv("GMAIL_APP_PASS") or os.getenv("GMAIL_APP_PASSWORD")

    msg = MIMEText(f"Hi {company}, offer for {location}")
    msg["Subject"] = f"Offer - {company}"
    msg["From"] = user
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as s:
        s.login(user,pw)
        s.send_message(msg)

def run():
    conn = sqlite3.connect(DB)
    leads = get_leads()
    print("ENGINE RUN:", len(leads))

    for id, co, em, loc in leads:
        try:
            send_email(em, co, loc)
            mark_sent(conn, id)
            print("SENT:", co, "| ENGINE:", ENGINE_NAME)
        except Exception as e:
            print("ERROR:", co, e)

if __name__ == "__main__":
    run()
