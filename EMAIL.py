import sqlite3, os, smtplib, time
from email.mime.text import MIMEText

U, P = os.getenv("GMAIL_USER"), os.getenv("GMAIL_PASS")
con = sqlite3.connect('titanium_system.db')
cur = con.cursor()

# BÁRMILYEN országból választunk 50 új leadet
query = "SELECT id, company_name, email, location FROM leads WHERE email IS NOT NULL AND email LIKE '%@%' AND status='new' LIMIT 50"
rows = cur.execute(query).fetchall()

if not rows:
    print("⚠️ Nincs több küldhető lead az adatbázisban."); exit()

print(f"🚀 GLOBÁLIS INDÍTÁS: {len(rows)} email küldése folyamatban...")

for i, (id, co, em, loc) in enumerate(rows, 1):
    body = f"Hi {co},\n\nI have 5 fresh leads for you in {loc}. Reply YES if you want them for free.\n\nFull access: https://titanium-v8-autopilot.onrender.com/\n\nBest regards, István"
    msg = MIMEText(body)
    msg["Subject"] = f"5 free leads for your business in {loc}"
    msg["From"] = U
    msg["To"] = em

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
            s.login(U, P)
            s.sendmail(U, [em], msg.as_string())
        cur.execute("UPDATE leads SET status='SENT' WHERE id=?", (id,))
        con.commit()
        print(f"✅ {i}/50 SENT: {em} ({loc})")
    except Exception as e:
        print(f"❌ {i}/50 HIBA ({em}): {e}")

    if i < len(rows):
        time.sleep(180) # 3 perc szünet a Google biztonság miatt
