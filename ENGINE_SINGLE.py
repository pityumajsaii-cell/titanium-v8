import sqlite3
import smtplib
import os
import time
from email.mime.text import MIMEText

DB = "titanium_system.db"

USER = os.getenv("GMAIL_USER")
PASS = os.getenv("GMAIL_APP_PASS")

ENGINE_NAME = "v54_single_engine"

con = sqlite3.connect(DB)
cur = con.cursor()

rows = cur.execute("""
SELECT id, company_name, email, location 
FROM leads 
WHERE status='new' AND email IS NOT NULL 
LIMIT 10
""").fetchall()

print(f"🚀 SINGLE ENGINE MODE START: {len(rows)} emails")

for i,(id,co,email,loc) in enumerate(rows,1):

    msg = MIMEText(f"Hi {co},\n\nQuick test offer.\nReply YES if interested.\n")
    msg["Subject"] = "Quick business test"
    msg["From"] = USER
    msg["To"] = email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as s:
            s.login(USER,PASS)
            s.send_message(msg)

        cur.execute("""
        UPDATE leads 
        SET status='SENT',
            last_sent_engine=? 
        WHERE id=?
        """,(ENGINE_NAME,id))

        con.commit()

        print(f"✅ SENT {i}/{len(rows)} → {email}")

    except Exception as e:
        print(f"❌ ERROR {email} → {e}")

    time.sleep(180)
