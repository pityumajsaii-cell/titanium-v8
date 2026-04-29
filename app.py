from flask import Flask, request, jsonify, send_file
app = Flask(__name__)

@app.route("/")
def home():
    return open("templates/index.html","r",encoding="utf-8").read()

@app.route("/api/leads", methods=["GET","POST"])
def leads():
    if request.method=="POST":
        data=request.json or {}
        return jsonify({"success":True,"received":data.get("count",0),"status":"saved"})
    return jsonify({"status":"online","endpoint":"/api/leads"})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
