import sqlite3
import random
import time

def generate_au_leads(count=500):
    conn = sqlite3.connect('titanium_system.db')
    cursor = conn.cursor()
    industries = ['FinTech', 'Mining Tech', 'AgriTech', 'Renewables', 'E-commerce']
    cities = ['Sydney, AU', 'Melbourne, AU', 'Brisbane, AU', 'Perth, AU']
    
    success = 0
    for _ in range(count):
        ts = int(time.time() * 1000) % 100000
        name = f"AU-Ent-{random.randint(1000, 9999)}-{ts}"
        loc = random.choice(cities)
        ind = random.choice(industries)
        score = random.randint(85, 99)
        try:
            cursor.execute("""
                INSERT INTO leads (company_name, location, industry, lead_score, source, status)
                VALUES (?, ?, ?, ?, 'AU-Expansion-Bot', 'new')
            """, (name, loc, ind, score))
            success += 1
        except:
            continue
    
    conn.commit()
    conn.close()
    print(f"✅ {success} egyedi ausztrál lead betöltve.")

if __name__ == "__main__":
    generate_au_leads(500)
