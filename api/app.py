from flask import Flask,request,jsonify
import sqlite3, os

app=Flask(__name__)
DB="titanium.db"

def q(sql,args=(),fetch=False):
    con=sqlite3.connect(DB)
    cur=con.cursor()
    cur.execute(sql,args)
    rows=cur.fetchall()
    con.commit()
    con.close()
    return rows if fetch else None

q("CREATE TABLE IF NOT EXISTS leads(id INTEGER PRIMARY KEY,name TEXT,email TEXT,city TEXT)")
q("CREATE TABLE IF NOT EXISTS revenue(id INTEGER PRIMARY KEY,amount REAL)")

@app.route("/")
def home():
    return {"status":"Titanium Online"}

@app.route("/lead",methods=["POST"])
def lead():
    d=request.json
    q("INSERT INTO leads(name,email,city) VALUES(?,?,?)",
      (d["name"],d["email"],d["city"]))
    return {"ok":True}

@app.route("/stats")
def stats():
    leads=q("SELECT COUNT(*) FROM leads",fetch=True)[0][0]
    rev=q("SELECT IFNULL(SUM(amount),0) FROM revenue",fetch=True)[0][0]
    return jsonify({"leads":leads,"revenue":rev})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=7860)
