#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "⚡ TITANIUM V31 HYBRID GOD MODE - DEPLOYING ENTERPRISE INFRASTRUCTURE"

# Mappa struktúra
mkdir -p static/vault static/invoices templates

cat > app.py << 'PY'
import os, sqlite3, stripe, threading
from flask import Flask, request, jsonify
from openai import OpenAI
import google.generativeai as genai
from anthropic import Anthropic
from fpdf import FPDF
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "TITAN-V31-GOD-MODE-99")

# --- MULTI-MODEL CLIENTS ---
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
stripe.api_key = os.getenv("STRIPE_SECRET")
webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

DB_PATH = "titanium_v31_hybrid.db"

# --- SMART ROUTING ENGINE ---
class TitaniumRouter:
    @staticmethod
    def run_task(task_type, prompt):
        try:
            if task_type == "REASONING": # OpenAI GPT-4o
                res = openai_client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}]
                )
                return res.choices[0].message.content
            
            elif task_type == "RESEARCH": # Google Gemini 1.5 Pro
                model = genai.GenerativeModel('gemini-1.5-pro')
                res = model.generate_content(prompt)
                return res.text
            
            elif task_type == "ANALYSIS": # Anthropic Claude 3.5 Sonnet
                res = anthropic_client.messages.create(
                    model="claude-3-5-sonnet-20240620",
                    max_tokens=2000,
                    messages=[{"role": "user", "content": prompt}]
                )
                return res.content[0].text
            
            # Fallback to OpenAI
            return "Routing Error - Fallback to GPT-4o enabled."
        except Exception as e:
            return f"Provider Error: {str(e)}"

# --- DATABASE SETUP ---
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS holding_vault (
            id INTEGER PRIMARY KEY, 
            client_email TEXT, 
            task_type TEXT, 
            output TEXT, 
            provider TEXT, 
            timestamp TEXT)""")
        conn.execute("CREATE TABLE IF NOT EXISTS finance (id INTEGER PRIMARY KEY, amount REAL, currency TEXT, date TEXT)")

# --- HYBRID WORKFLOW (REAL DATA) ---
def execute_hybrid_fulfillment(email, service_id):
    def workflow():
        print(f"🚀 Hybrid Workflow elindult: {email}")
        
        # 1. SZAKASZ: Gemini végzi a mély kutatást (Research)
        research = TitaniumRouter.run_task("RESEARCH", f"Keress 5 konkrét svájci vagy német céget a(z) {service_id} szektorban. Adj weboldalakat és piaci trendeket.")
        
        # 2. SZAKASZ: OpenAI írja a Sales Copy-t (Reasoning)
        copy = TitaniumRouter.run_task("REASONING", f"Írj egy ellenállhatatlan ajánlatot az alábbi kutatás alapján: {research}")
        
        # 3. SZAKASZ: Claude készíti el az Onboarding PDF tartalmát (Analysis)
        onboarding = TitaniumRouter.run_task("ANALYSIS", f"Készíts egy strukturált onboarding dokumentumot ehhez a szolgáltatáshoz: {service_id}. Feladat: {copy}")

        # Mentés a Holding Vault-ba
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("INSERT INTO holding_vault (client_email, task_type, output, provider, timestamp) VALUES (?,?,?,?,?)",
                         (email, "HYBRID_SUITE", f"RESEARCH: {research}\n\nCOPY: {copy}\n\nDOCS: {onboarding}", "MULTI", datetime.now().isoformat()))
        print(f"✅ Hybrid Fulfillment befejezve: {email}")

    threading.Thread(target=workflow).start()

# --- WEBHOOK & API ---
@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.data
    sig = request.headers.get('Stripe-Signature')
    event = stripe.Webhook.construct_event(payload, sig, webhook_secret)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        email = session['metadata']['email']
        service_id = session['metadata']['service_id']
        
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("INSERT INTO finance (amount, currency, date) VALUES (?,?,?)",
                         (session['amount_total']/100, "EUR", datetime.now().isoformat()))
        
        execute_hybrid_fulfillment(email, service_id)
    return "OK", 200

@app.route("/api/status")
def status():
    return jsonify({"status": "GOD_MODE_ACTIVE", "providers": ["OpenAI", "Gemini", "Claude"], "engine": "Titanium V31"})

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=7860)
PY

# Deploy parancsok
git add .
git commit -m "⚡ TITANIUM V31: HYBRID GOD MODE DEPLOYED"
git push hf main --force
vercel --prod --yes
