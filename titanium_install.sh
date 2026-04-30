#!/data/data/com.termux/files/usr/bin/bash

echo "===================================="
echo "🔥 TITANIUM FULL INSTALLER"
echo "===================================="

# ----------------------------
# 1. PYTHON + FLASK INSTALL
# ----------------------------
echo "[1] Installing Python + Flask..."
pkg update -y
pkg install python -y
pip install flask gunicorn --quiet

# ----------------------------
# 2. PROJECT FOLDER
# ----------------------------
mkdir -p ~/TitaniumOne
cd ~/TitaniumOne

# ----------------------------
# 3. APP.PY (FULL FIXED SYSTEM)
# ----------------------------
echo "[2] Creating app.py..."

cat > app.py <<'PY'
from flask import Flask, request, jsonify

app = Flask(__name__)

# ================= UI =================
@app.route("/")
def home():
    return """
    <h1>🔥 TITANIUM SYSTEM ONLINE</h1>
    <p>Webhook + Health + UI active</p>
    """, 200


# ================= HEALTH =================
@app.route("/health")
def health():
    return jsonify(status="ok", system="titanium"), 200


# ================= WEBHOOK =================
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    print("🔥 WEBHOOK:", data)

    # future: stripe / db / queue
    return jsonify(success=True), 200


# ================= START =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
PY

# ----------------------------
# 4. PROCFILE (RENDER FIX)
# ----------------------------
echo "[3] Creating Procfile..."
echo "web: gunicorn app:app --bind 0.0.0.0:\$PORT" > Procfile

# ----------------------------
# 5. OPTIONAL GIT INIT
# ----------------------------
if [ ! -d .git ]; then
    git init
fi

git add app.py Procfile
git commit -m "titanium full install fix" 2>/dev/null || true

# ----------------------------
# 6. DONE
# ----------------------------
echo "===================================="
echo "✅ INSTALL COMPLETE"
echo "===================================="
echo ""
echo "START LOCAL SERVER:"
echo "cd ~/TitaniumOne && python app.py"
echo ""
echo "TEST:"
echo "http://localhost:8080"
echo ""
echo "RENDER START COMMAND:"
echo "gunicorn app:app --bind 0.0.0.0:\$PORT"
echo "===================================="
