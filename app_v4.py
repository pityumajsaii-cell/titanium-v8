import sqlite3, os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)

PORT=int(os.getenv("APP_PORT",5000))
PASS=os.getenv("ADMIN_PASS")

@app.route("/")
def home():
    db=sqlite3.connect(timeout=30, "data/titanium.db")
    c=db.cursor()

    leads=c.execute("SELECT count(*) FROM leads").fetchone()[0]
    won=c.execute("SELECT count(*) FROM leads WHERE status='won'").fetchone()[0]
    rev=c.execute("SELECT IFNULL(sum(amount),0) FROM revenue").fetchone()[0]

    db.close()

    return f"""
    <html><body style='background:#111;color:#fff;padding:40px;font-family:Arial'>
    <h1>🔥 TITANIUM V4 AUTO MONEY</h1>
    <hr>
    <p>Total Leads: {leads}</p>
    <p>Closed Deals: {won}</p>
    <p>Revenue: €{rev}</p>
    <p>Status: AUTOPILOT ACTIVE</p>
    <hr>
    <a href='/admin'>Admin</a>
    </body></html>
    """

@app.route("/admin")
def admin():
    return "Use ?pass=yourpass"

@app.route("/admin/<pw>")
def realadmin(pw):
    if pw != PASS:
        return "Denied"

    db=sqlite3.connect(timeout=30, "data/titanium.db")
    c=db.cursor()

    rows=c.execute("""
    SELECT client,amount,source FROM revenue
    ORDER BY id DESC LIMIT 20
    """).fetchall()

    html="<html><body><h1>Revenue</h1>"

    for r in rows:
        html+=f"<p>{r[0]} - €{r[1]} - {r[2]}</p>"

    html+="</body></html>"
    db.close()
    return html

app.run(host="0.0.0.0",port=PORT)
