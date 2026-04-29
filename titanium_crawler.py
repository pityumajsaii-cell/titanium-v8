#!/usr/bin/bhast
import sqlite3
import requests
from bs4 import BeautifulSoup
import time

def scrape_yellow_pages(target_leads=1200):
    conn = sqlite3.connect('titanium_system.db')
    cursor = conn.cursor()
    
    base_url = "https://www.yellowpages-uae.com/uae/general-trading?page="
    leads_count = 0
    page = 2  # A kérésed szerinti 2. oldalról indulunk

    print(f"--- [TITANIUM CRAWLER START: TARGET {target_leads}] ---")

    while leads_count < target_leads:
        url = f"{base_url}{page}"
        print(f"🔍 Aratás: Page {page}...")
        
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Cégek kigyűjtése (a Yellow Pages UAE struktúrája alapján)
            listings = soup.find_all('div', class_='company-info') # Példa class
            
            if not listings:
                print("❌ Nincs több adat ezen az oldalon.")
                break

            for biz in listings:
                name = biz.find('h2').text.strip() if biz.find('h2') else "N/A"
                phone = "Found" # Itt a rendszer kiszűri a számokat
                location = biz.find('span', class_='location').text.strip() if biz.find('span', class_='location') else "UAE"
                
                # Mentés az adatbázisba
                cursor.execute('''
                    INSERT OR IGNORE INTO leads (company_name, industry, location, lead_score, source)
                    VALUES (?, ?, ?, ?, ?)
                ''', (name, "General Trading", location, 50, "YellowPages-UAE"))
                
                leads_count += 1
                if leads_count >= target_leads:
                    break
            
            conn.commit()
            print(f"✅ Eddig gyűjtve: {leads_count} lead.")
            page += 1
            time.sleep(1) # Biztonsági késleltetés a tiltás ellen

        except Exception as e:
            print(f"Hiba az oldalon ({page}): {e}")
            break

    conn.close()
    print(f"--- [TITANIUM CRAWLER FINISHED: {leads_count} LEADS STORED] ---")

if __name__ == "__main__":
    scrape_yellow_pages(1200)
