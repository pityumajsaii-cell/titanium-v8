import sqlite3, datetime, random

DB="hunter_v4.db"

SWISS = [
("Nestle","contact@nestle.com","Vevey","Switzerland","Food","https://nestle.com"),
("Roche","info@roche.com","Basel","Switzerland","Pharma","https://roche.com"),
("Novartis","info@novartis.com","Basel","Switzerland","Pharma","https://novartis.com"),
("ABB","contact@abb.com","Zurich","Switzerland","Technology","https://abb.com"),
("UBS","info@ubs.com","Zurich","Switzerland","Finance","https://ubs.com"),
("Credit Suisse","info@credit-suisse.com","Zurich","Switzerland","Finance","https://credit-suisse.com"),
("Swiss Re","contact@swissre.com","Zurich","Switzerland","Insurance","https://swissre.com"),
("Zurich Insurance","info@zurich.com","Zurich","Switzerland","Insurance","https://zurich.com"),
("Richemont","contact@richemont.com","Geneva","Switzerland","Luxury","https://richemont.com"),
("Logitech","info@logitech.com","Lausanne","Switzerland","Hardware","https://logitech.com"),
]

USA = [
("Apple","contact@apple.com","Cupertino","USA","Technology","https://apple.com"),
("Microsoft","info@microsoft.com","Redmond","USA","Software","https://microsoft.com"),
("Amazon","contact@amazon.com","Seattle","USA","Ecommerce","https://amazon.com"),
("Google","info@google.com","Mountain View","USA","Tech","https://google.com"),
("NVIDIA","contact@nvidia.com","Santa Clara","USA","AI Hardware","https://nvidia.com"),
("Tesla","info@tesla.com","Austin","USA","Automotive","https://tesla.com"),
("Meta","contact@meta.com","Menlo Park","USA","Social Media","https://meta.com"),
("Oracle","info@oracle.com","Austin","USA","Software","https://oracle.com"),
("Salesforce","contact@salesforce.com","San Francisco","USA","CRM","https://salesforce.com"),
("Intel","info@intel.com","Santa Clara","USA","Semiconductor","https://intel.com"),
]

def ensure():
    con=sqlite3.connect(timeout=30, DB)
    cur=con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS leads(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created TEXT,
        company TEXT,
        email TEXT,
        city TEXT,
        country TEXT,
        niche TEXT,
        website TEXT,
        status TEXT,
        owner TEXT,
        notes TEXT
    )
    """)
    con.commit()
    con.close()

def load():
    ensure()
    con=sqlite3.connect(timeout=30, DB)
    cur=con.cursor()

    rows=[]
    for i in range(100):
        c=random.choice(SWISS)
        rows.append(c)

    for i in range(100):
        c=random.choice(USA)
        rows.append(c)

    total=0
    for r in rows:
        created=str(datetime.datetime.now())
        company,email,city,country,niche,website=r
        company=f"{company} {random.randint(1,999)}"

        cur.execute("""
        INSERT INTO leads(
        created,company,email,city,country,niche,website,status,owner,notes
        ) VALUES(?,?,?,?,?,?,?,?,?,?)
        """,(
        created,company,email,city,country,niche,website,
        "NEW","TITANIUM","CH_US_IMPORT"
        ))
        total+=1

    con.commit()
    con.close()
    print("✅ Added:",total,"real-style CH + USA leads")

if __name__=="__main__":
    load()
