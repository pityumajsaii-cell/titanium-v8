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
