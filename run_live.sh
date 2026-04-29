#!/data/data/com.termux/files/usr/bin/bash
cd ~/TitaniumOne
python3 core/init_db.py
python3 core/load_services.py
python3 app.py
