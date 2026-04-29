import sqlite3,time,datetime,random

DB="titanium.db"

PITCHES = [
"AI lead generation system that books qualified appointments automatically.",
"Done-for-you client acquisition funnel with automated follow-up.",
"Revenue growth system for premium businesses using AI + automation.",
"High-ticket customer pipeline setup with fast implementation.",
"Missed-lead recovery + appointment booking automation."
]

def run():
    con=sqlite3.connect(DB)
    cur=con.cursor()

    rows=cur.execute("""
    SELECT id,name,email,country
    FROM elite_leads
    WHERE status='NEW'
    LIMIT 100
    """).fetchall()

    sent=0

    for row in rows:
        id_,name,email,country=row
        pitch=random.choice(PITCHES)

        print("📤 SEND:",name,"|",email,"|",country)
        print("💰 OFFER:",pitch)
        print("-----")

        cur.execute("""
        UPDATE elite_leads
        SET status='SENT'
        WHERE id=?
        """,(id_,))

        sent+=1
        time.sleep(0.2)

    con.commit()
    con.close()

    print("🔥 DONE:",sent,"elite leads processed")

if __name__=="__main__":
    run()
