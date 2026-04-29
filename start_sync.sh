#!/bin/bash
while true; do
    sqlite3 -header -csv ~/TitaniumOne/titanium_system.db "SELECT * FROM leads;" > ~/TitaniumOne/leads_dataset.csv
    python3 ~/TitaniumOne/ai_analyze.py
    git add ~/TitaniumOne/leads_dataset.csv ~/TitaniumOne/elite_targets.csv
    git commit -m "Titanium Auto-Sync: $(date)"
    git push origin main
    sleep 3600
done
