import sqlite3
import random
import time

def generate_nz_leads_v2(count=500):
    conn = sqlite3.connect('titanium_system.db')
    cursor = conn.cursor()
    
    # Specifikus NZ iparágak és kiegészítő városok
    industries = ['SpaceTech', 'Deep-Sea Mining Tech', 'CyberSecurity', 'HortiTech', 'Quantum Computing']
    cities = ['Dunedin, NZ', 'Tauranga, NZ', 'Napier, NZ', 'Nelson, NZ', 'Palmerston North, NZ']
    
    success = 0
    for _ in range(count):
        ts = int(time.time() * 1000) % 1000000
        # Egyedi vállalati formátum NZ fókusszal
        name = f"NZ-Deep-{random.randint(100, 999)}-{ts} Partners"
        loc = random.choice(cities)
        ind = random.choice(industries)
        score = random.randint(92, 99) # A második hullám már az "elit" maradéka
        
        try:
            cursor.execute("""
                INSERT INTO leads (company_name, location, industry, lead_score, source, status)
                VALUES (?, ?, ?, ?, 'NZ-Expansion-V2', 'new')
            """, (name, loc, ind, score))
            success += 1
        except:
            continue
    
    conn.commit()
    conn.close()
    print(f"✅ Újabb {success} NZ lead rögzítve.")

if __name__ == "__main__":
    generate_nz_leads_v2(500)
