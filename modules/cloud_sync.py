import sqlite3, requests, datetime, json

DB="titanium.db"

RENDER_URL="https://titanium-v8-autopilot.onrender.com/api/leads"
HF_URL="https://Pityumajsaii-Titanium.hf.space/api/leads"

def get_rows():
    con=sqlite3.connect(DB)
    cur=con.cursor()
    try:
        rows=cur.execute("""
        SELECT id,created,name,email,country,service,notes,status
        FROM leads ORDER BY id DESC LIMIT 200
        """).fetchall()
    except:
        rows=[]
    con.close()
    return rows

def push(url,payload):
    try:
        r=requests.post(url,json=payload,timeout=25)
        return r.status_code, r.text[:200]
    except Exception as e:
        return "ERR", str(e)

def run():
    rows=get_rows()
    leads=[]
    for r in rows:
        leads.append({
            "id":r[0],
            "created":r[1],
            "name":r[2],
            "email":r[3],
            "country":r[4],
            "service":r[5],
            "notes":r[6],
            "status":r[7]
        })

    payload={
        "time":datetime.datetime.now(datetime.UTC).isoformat(),
        "count":len(leads),
        "leads":leads
    }

    print("🔥 RENDER:", push(RENDER_URL,payload))
    print("🤗 HF:", push(HF_URL,payload))

if __name__=="__main__":
    run()
