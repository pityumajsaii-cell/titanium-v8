#!/data/data/com.termux/files/usr/bin/bash
cd ~/TitaniumOne
./save_now.sh
python3 core/init_db.py
python3 app.py
