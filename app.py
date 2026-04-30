from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "TITANIUM ONLINE", 200

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    print("WEBHOOK:", data)
    return jsonify(ok=True), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
