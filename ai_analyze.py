import pandas as pd
import os

try:
    if os.path.exists('leads_dataset.csv'):
        df = pd.read_csv('leads_dataset.csv')
        df.columns = df.columns.str.strip().str.lower()
        
        # Keressük meg az oszlopokat (index alapján is biztosítva)
        # A te sémád szerint: 4. loc (index 4), 7. score (index 7)
        score_col = 'lead_score' if 'lead_score' in df.columns else df.columns[7]
        loc_col = 'location' if 'location' in df.columns else df.columns[4]

        # KRITIKUS JAVÍTÁS: Kényszerített numerikus típus
        df[score_col] = pd.to_numeric(df[score_col], errors='coerce').fillna(0)
        
        # Elit szűrés
        elite = df[(df[score_col] >= 95) & (df[loc_col].str.contains('ch|dubai|uae', case=False, na=False))]
        elite.to_csv('elite_targets.csv', index=False)
        print(f"✅ AI Siker: {len(elite)} elit célpont rögzítve.")
    else:
        print("❌ CSV nem található.")
except Exception as e:
    print(f"❌ Hiba: {e}")
