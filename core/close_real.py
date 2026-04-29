import sqlite3, sys

if len(sys.argv) < 3:
    print('HASZNÁLAT: python3 core/close_real.py "Cég" 199000')
    exit()

company = sys.argv[1]
amount = int(sys.argv[2])

db = sqlite3.connect("data/titanium.db")
c = db.cursor()

# Itt a státusz már 'paid' - ez a valódi cash
c.execute("INSERT INTO sales(company,amount,status) VALUES(?,?,'paid')",(company,amount))
c.execute("UPDATE leads SET status='won' WHERE company=?",(company,))

db.commit()
db.close()
print(f"✅ REAL CASH RECORDED: {company} | {amount} FT")
