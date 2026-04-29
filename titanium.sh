#!/data/data/com.termux/files/usr/bin/bash

case $1 in
start)
python api/app.py
;;
lead)
curl -X POST http://127.0.0.1:7860/lead \
-H "Content-Type: application/json" \
-d '{"name":"Swiss Dental","email":"info@clinic.ch","city":"Zurich"}'
;;
stats)
curl http://127.0.0.1:7860/stats
;;
esac
