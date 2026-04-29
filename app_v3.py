import sqlite3, os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)

PORT=int(os.getenv("APP_PORT",5000))
PASS=os.getenv("ADMIN_PASS")
COMPANY=os.getenv("COMPANY_NAME")
PAY=os.getenv("STRIPE_LINK")

@app.route("/")
def home():
    db=sqlite3.connect(timeout=30, "data/titanium.db")
    c=db.cursor()
    rows=c.execute("SELECT name,category,price FROM services ORDER BY category").fetchall()
    db.close()

    html=f"<html><body style='background:#111;color:#fff;padding:40px;font-family:Arial'>"
    html+=f"<h1>🔥 {COMPANY}</h1>"
    html+="<h2>40+ AI Services Marketplace</h2><hr>"

    for r in rows:
        html+=f"<p><b>{r[0]}</b> [{r[1]}] - €{r[2]} <a href='{PAY}'>BUY</a></p>"

    html+="""
    <hr>
    <h2>Request Custom Quote</h2>
    <form method='post' action='/lead'>
    <input name='name' placeholder='Name'><br><br>
    <input name='email' placeholder='Email'><br><br>
    <input name='company' placeholder='Company'><br><br>
    <input name='service' placeholder='Wanted Service'><br><br>
    <button>Send</button>
    </form>
    <br><a href='/admin'>Admin</a>
    </body></html>
    """
    return html

@app.route("/lead",methods=["POST"])
def lead():
    db=sqlite3.connect(timeout=30, "data/titanium.db")
    c=db.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS leads(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,email TEXT,company TEXT,service TEXT,status TEXT DEFAULT 'new'
    )
    """)

    c.execute("""
    INSERT INTO leads(name,email,company,service)
    VALUES(?,?,?,?)
    """,(
        request.form["name"],
        request.form["email"],
        request.form["company"],
        request.form["service"]
    ))

    db.commit()
    db.close()

    return "<h1>Quote request received</h1>"

@app.route("/admin")
def admin():
    if request.args.get("pass","") != PASS:
        return "Denied"

    db=sqlite3.connect(timeout=30, "data/titanium.db")
    c=db.cursor()

    leads=c.execute("SELECT count(*) FROM leads").fetchone()[0]
    services=c.execute("SELECT count(*) FROM services").fetchone()[0]

    html=f"""
    <html><body>
    <h1>🔥 TITANIUM ADMIN</h1>
    <p>Total Services: {services}</p>
    <p>Total Leads: {leads}</p>
    </body></html>
    """

    db.close()
    return html

app.run(host="0.0.0.0",port=PORT)
