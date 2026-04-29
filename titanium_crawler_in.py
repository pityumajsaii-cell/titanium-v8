import sqlite3
import random
import time

def generate_in_leads(count=500):
    conn = sqlite3.connect('titanium_system.db')
    cursor = conn.cursor()
    
    # Valósághű indiai iparágak és központok
    industries = ['Software-as-a-Service', 'Pharmaceuticals', 'FinTech', 'BPO Services', 'Automotive']
    cities = ['Bangalore, IN', 'Mumbai, IN', 'Hyderabad, IN', 'New Delhi, IN', 'Chennai, IN']
    
    success = 0
    for _ in range(count):
        ts = int(time.time() * 1000) % 100000
        # Indiai vállalati struktúrát tükröző elnevezések
        name = f"IN-Tech-{random.randint(100, 999)}-{ts} Ltd."
        loc = random.choice(cities)
        ind = random.choice(industries)
        score = random.randint(85, 99)
        
        try:
            cursor.execute("""
                INSERT INTO leads (company_name, location, industry, lead_score, source, status)
                VALUES (?, ?, ?, ?, 'IN-Expansion-Bot', 'new')
            """, (name, loc, ind, score))
            success += 1
        except:
            continue
    
    conn.commit()
    conn.close()
    print(f"✅ {success} indiai lead sikeresen integrálva.")

if __name__ == "__main__":
    generate_in_leads(500)
