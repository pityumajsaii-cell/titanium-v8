from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "TITANIUM ONLINE OK", 200

@app.route("/health")
def health():
    return jsonify(status="ok", system="titanium"), 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    print("WEBHOOK RECEIVED:", data)
    return jsonify(ok=True), 200

# Render compatibility debug endpoint
@app.route("/debug")
def debug():
    return {
        "routes": [str(r) for r in app.url_map.iter_rules()]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
