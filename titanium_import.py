#!/usr/bin/bhast
import sqlite3

def run_titanium_import():
    combined_leads = [
        ("Horizon Signal Technologies, Inc.", "https://horizonsignal.com", "Manufacturer", "Reading, PA", "Over $250M", "10-49", 95, "Thomasnet"),
        ("Moog Inc.", "https://moog.com", "Manufacturer", "Elma, NY", "Over $250M", "1000+", 90, "Thomasnet"),
        ("IFM Efector, Inc.", "https://ifm.com", "Manufacturer / Distributor", "Malvern, PA", "$100M-$249.9M", "1000+", 85, "Thomasnet"),
        ("Broadcom Corp.", "https://broadcom.com", "Manufacturer", "San Jose, CA", "Over $250M", "1000+", 85, "Thomasnet"),
        ("Moore Industries International, Inc.", "https://miinet.com", "Manufacturer", "North Hills, CA", "$50M-$99.9M", "200-499", 80, "Thomasnet"),
        ("Belt-Way Scales, Inc.", "https://beltwayscales.com", "Manufacturer", "Rock Falls, IL", "$10M-$24.9M", "50-99", 75, "Thomasnet"),
        ("Banner Industries", "https://bannerindustries.com", "Distributor", "Danvers, MA", "$10M-$24.9M", "10-49", 70, "Thomasnet"),
        ("Ahammed Jadeer General Trading LLC", "N/A", "General Trading", "Dubai, Silicon Oasis", "Unknown", "N/A", 80, "UAE Directory"),
        ("PHG General Trading Kft.", "N/A", "General Trading / Construction", "Dubai, Hor Al Anz", "Unknown", "N/A", 75, "UAE Directory"),
        ("Royal Fifty3 Kft.", "N/A", "General Trading", "Sharjah, Media City", "Unknown", "N/A", 70, "UAE Directory"),
        ("Al Ahsa General Trading LLC", "N/A", "General Trading", "Dubai, Zarooni Bldg", "Unknown", "N/A", 65, "UAE Directory"),
        ("Al Aman Catering Services LLC", "N/A", "Hospitality / Catering", "Abu Dhabi, Al Nahyan", "Unknown", "N/A", 60, "UAE Directory")
    ]

    try:
        conn = sqlite3.connect('titanium_system.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT UNIQUE,
                website TEXT,
                industry TEXT,
                location TEXT,
                revenue TEXT,
                employees TEXT,
                lead_score INTEGER,
                source TEXT,
                status TEXT DEFAULT 'new',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.executemany('''
            INSERT OR IGNORE INTO leads
            (company_name, website, industry, location, revenue, employees, lead_score, source)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', combined_leads)
        count = cursor.rowcount
        conn.commit()
        conn.close()
        print("\n--- [TITANIUM SYSTEM STATUS] ---")
        print(f"Sikeresen integrálva: {count} új lead.")
        print("Státusz: Kész a profit-generálásra.")
        print("--------------------------------\n")
    except Exception as e:
        print(f"Hiba: {e}")

if __name__ == "__main__":
    run_titanium_import()
