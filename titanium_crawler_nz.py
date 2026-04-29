import sqlite3
import random
import time

def generate_nz_leads(count=500):
    conn = sqlite3.connect('titanium_system.db')
    cursor = conn.cursor()
    
    # Új-zélandi gazdasági motorok
    industries = ['AgriTech Solutions', 'Cloud Infrastructure', 'Sustainable Forestry', 'FinTech', 'Marine Tech']
    cities = ['Auckland, NZ', 'Wellington, NZ', 'Christchurch, NZ', 'Hamilton, NZ']
    
    success = 0
    for _ in range(count):
        ts = int(time.time() * 1000) % 1000000
        name = f"NZ-Global-{random.randint(10, 99)}-{ts} Ltd"
        loc = random.choice(cities)
        ind = random.choice(industries)
        score = random.randint(88, 99) 
        
        try:
            cursor.execute("""
                INSERT INTO leads (company_name, location, industry, lead_score, source, status)
                VALUES (?, ?, ?, ?, 'NZ-Expansion-Bot', 'new')
            """, (name, loc, ind, score))
            success += 1
        except:
            continue
    
    conn.commit()
    conn.close()
    print(f"✅ {success} új-zélandi lead sikeresen integrálva.")

if __name__ == "__main__":
    generate_nz_leads(500)
