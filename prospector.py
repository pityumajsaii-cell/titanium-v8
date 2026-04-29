import csv

def create_lead_list():
    print("🚀 TITANIUM PROSPECTOR ELINDÍTVA")
    target_city = "Tolna és környéke" # Ezt bármikor átírhatod Londonra vagy New Yorkra
    
    # Első körös célpont minták (Pl: helyi vállalkozások)
    prospects = [
        ["Cégnév", "Email/Kontakt", "Iparág", "Státusz"],
        ["Helyi Étterem 1", "info@ettermem.hu", "Vendéglátás", "NEW"],
        ["Autószerviz X", "szerviz@auto.hu", "Szolgáltatás", "NEW"],
        ["Kereskedő Y", "sales@bolt.hu", "Retail", "NEW"]
    ]
    
    with open("prospects.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(prospects)
    
    print(f"✅ Célpont lista létrehozva: prospects.csv ({target_city})")
    print("👉 Következő lépés: AI Outreach üzenetek generálása.")

if __name__ == "__main__":
    create_lead_list()
