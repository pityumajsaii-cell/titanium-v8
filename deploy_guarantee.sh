#!/bin/bash
echo "🚀 [TDG] STARTING DEPLOYMENT..."

# 1. Kód és Procfile ellenőrzés
echo "web: gunicorn app:app --bind 0.0.0.0:\$PORT" > Procfile

# 2. Git Push
git add .
git commit -m "🚀 TDG: Production stable sync with health routes"
git push origin main

echo "⏳ [TDG] WAITING FOR RENDER BUILD (60s)..."
sleep 60

# 3. Health Check Validator
STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://titanium-v8-autopilot.onrender.com/health)

if [ "$STATUS" -eq 200 ]; then
    echo "✅ [TDG] SUCCESS: System is LIVE and HEALTHY!"
else
    echo "❌ [TDG] ERROR: Still getting $STATUS. Please do Manual 'Clear Cache & Deploy' on Render!"
fi
