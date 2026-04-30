#!/data/data/com.termux/files/usr/bin/bash

echo "===================================="
echo "🔥 TITANIUM SELF-HEAL V2"
echo "===================================="

cd ~/TitaniumOne || exit 1

echo "[1] Fix app.py..."

cat > app.py <<'PY'
from flask import Flask, request, jsonify

app = Flask(__name__)

# ================= ROOT =================
@app.route("/")
def home():
    return "TITANIUM ONLINE OK", 200

# ================= HEALTH =================
@app.route("/health")
def health():
    return jsonify(status="ok", system="titanium"), 200

# ================= WEBHOOK =================
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    print("WEBHOOK RECEIVED:", data)
    return jsonify(ok=True), 200

# ================= DEBUG ROUTES =================
@app.route("/routes")
def routes():
    return {
        "routes": [str(r) for r in app.url_map.iter_rules()]
    }

# ================= START =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
PY

echo "[2] Fix Procfile..."
echo "web: gunicorn app:app --bind 0.0.0.0:\$PORT" > Procfile

echo "[3] Git sync..."
git add .
git commit -m "SELF-HEAL V2 FIX" 2>/dev/null || echo "No changes"
git push origin main --force 2>/dev/null || echo "Push skipped"

echo ""
echo "===================================="
echo "✅ LOCAL TEST COMMAND:"
echo "cd ~/TitaniumOne && python app.py"
echo ""
echo "===================================="
echo "🚀 RENDER FIX REQUIRED:"
echo "Settings → Start Command:"
echo "gunicorn app:app --bind 0.0.0.0:\$PORT"
echo ""
echo "Then:"
echo "Manual Deploy → Clear cache & deploy"
echo "===================================="
