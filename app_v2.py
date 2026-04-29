import sqlite3, os
from flask import Flask, request, redirect
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

PORT=int(os.getenv("APP_PORT",5000))
PASS=os.getenv("ADMIN_PASS")
COMPANY=os.getenv("COMPANY_NAME")
PAY=os.getenv("STRIPE_LINK")

@app.route("/")
def home():
    db=sqlite3.connect(timeout=30, "data/titanium.db")
    c=db.cursor()
    services=c.execute("SELECT name,price,description FROM services").fetchall()
    db.close()

    html=f"<html><body style='background:#111;color:#fff;padding:40px;font-family:Arial'><h1>🔥 {COMPANY}</h1><hr>"

    for s in services:
        html += f"<p><b>{s[0]}</b> - €{s[1]}<br>{s[2]}<br><a href='{PAY}'>BUY NOW</a></p><hr>"

    html += """
    <h2>Free Consultation</h2>
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

@app.route("/lead", methods=["POST"])
def lead():
    db=sqlite3.connect(timeout=30, "data/titanium.db")
    c=db.cursor()

    c.execute("""
    INSERT INTO leads(name,email,company,service,status)
    VALUES(?,?,?,?, 'new')
    """,(
        request.form["name"],
        request.form["email"],
        request.form["company"],
        request.form["service"]
    ))

    db.commit()
    db.close()

    return "<h1>Lead received.</h1><a href='/'>Back</a>"

@app.route("/admin")
def admin():
    if request.args.get("pass","") != PASS:
        return "<h1>Denied. use ?pass=yourpass</h1>"

    db=sqlite3.connect(timeout=30, "data/titanium.db")
    c=db.cursor()

    leads=c.execute("SELECT count(*) FROM leads").fetchone()[0]
    new=c.execute("SELECT count(*) FROM leads WHERE status='new'").fetchone()[0]
    contacted=c.execute("SELECT count(*) FROM leads WHERE status='contacted'").fetchone()[0]
    fu=c.execute("SELECT count(*) FROM followups").fetchone()[0]

    html=f"""
    <html><body>
    <h1>🔥 TITANIUM CRM</h1>
    <p>Total Leads: {leads}</p>
    <p>New: {new}</p>
    <p>Contacted: {contacted}</p>
    <p>Followups: {fu}</p>
    </body></html>
    """

    db.close()
    return html

app.run(host="0.0.0.0",port=PORT)
