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
