from flask import Flask, request

app = Flask(__name__)

# ---------------- UI ----------------
@app.route("/")
def home():
    return """
    <h1>TITANIUM SYSTEM ACTIVE</h1>
    <p>Webhook + UI unified server running</p>
    """, 200

# ---------------- WEBHOOK ----------------
@app.route("/webhook", methods=["POST"])
def webhook():
    event = request.json
    print("WEBHOOK EVENT:", event)
    return "ok", 200

# ---------------- HEALTH ----------------
@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
