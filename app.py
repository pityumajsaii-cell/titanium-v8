from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "TITANIUM V8 - SAAS-MABX ACTIVE", 200

@app.route("/health")
def health():
    return jsonify(status="ok", engine="Titanium-V8", instance="saas-mabx"), 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    print(f"🔥 WEBHOOK RECEIVED: {data}")
    return jsonify(success=True, received=True), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
