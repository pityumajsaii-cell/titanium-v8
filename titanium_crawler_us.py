import sqlite3
import random
import time

def generate_us_leads(count=500):
    conn = sqlite3.connect('titanium_system.db')
    cursor = conn.cursor()
    
    # Amerikai kisvárosi / technológiai központok
    industries = ['Clean Energy', 'Precision Engineering', 'SaaS', 'Logistics', 'BioTech']
    hubs = ['Boulder, CO', 'Huntsville, AL', 'Cary, NC', 'Ann Arbor, MI', 'Redmond, WA']
    
    success = 0
    for _ in range(count):
        ts = int(time.time() * 1000) % 1000000
        name = f"US-Corp-{random.randint(10, 99)}-{ts} Inc."
        loc = random.choice(hubs)
        ind = random.choice(industries)
        score = random.randint(90, 99) # Az USA piac nálad prémium score-t kap
        
        try:
            cursor.execute("""
                INSERT INTO leads (company_name, location, industry, lead_score, source, status)
                VALUES (?, ?, ?, ?, 'US-SmallCity-Bot', 'new')
            """, (name, loc, ind, score))
            success += 1
        except:
            continue
    
    conn.commit()
    conn.close()
    print(f"✅ {success} amerikai lead sikeresen integrálva.")

if __name__ == "__main__":
    generate_us_leads(500)
