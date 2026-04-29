#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "💰 TITANIUM REAL MONEY V1 - AKTÍV BEVÉTELI RENDSZER"

# Biztonságos struktúra
mkdir -p leads contracts invoices

cat > app.py << 'PY'
import os, sqlite3, stripe, requests, threading
from flask import Flask, request, jsonify
from openai import OpenAI
import google.generativeai as genai
from datetime import datetime

# --- KONFIGURÁCIÓ (Használd a .env fájlt!) ---
load_dotenv()
stripe.api_key = os.getenv("STRIPE_SECRET")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

# --- 1. AZ ÜGYFÉLVADÁSZ (SCRAPER) ---
def hunt_leads(niche, location):
    """
    Ez a modul szimulált, de a logikája helyes: 
    Google Maps API vagy Web Scraping kell ide a valódi adatokhoz.
    """
    prompt = f"Adj 5 létező cégnevet és elérhetőséget: {niche} - {location}. Csak valós adatokkal."
    model = genai.GenerativeModel('gemini-1.5-pro')
    res = model.generate_content(prompt)
    return res.text

# --- 2. AZ AUTOMATA ÉRTÉKESÍTŐ (OUTREACH) ---
def send_ai_proposal(email, niche):
    """
    Itt küldené ki a rendszer a Mailgun/SendGrid API-n keresztül a levelet.
    """
    proposal = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Profi B2B értékesítő vagy."},
                  {"role": "user", "content": f"Írj egy ellenállhatatlan ajánlatot {niche} számára, ami a 299 eurós AI Lead Engine-ről szól."}]
    )
    # Logoljuk a kiküldést
    with open("outreach_log.txt", "a") as f:
        f.write(f"{datetime.now()}: Ajánlat küldve ide: {email}\n")
    return proposal.choices[0].message.content

# --- 3. A KASSZA (STRIPE & DB) ---
@app.route("/pay", methods=["POST"])
def pay():
    data = request.json
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{'price_data': {'currency': 'eur', 'product_data': {'name': data['niche']}, 'unit_amount': 29900}, 'quantity': 1}],
            mode='payment',
            success_url="https://titanium-v1.vercel.app/success",
            cancel_url="https://titanium-v1.vercel.app/cancel",
        )
        return jsonify({"url": session.url})
    except Exception as e:
        return jsonify(error=str(e)), 400

# --- CRM & ADMIN ---
@app.route("/admin/status")
def status():
    return "<h1>REAL MONEY V1: RENDSZER ÜZEMKÉSZ</h1><p>Várjuk az első 299 EUR-t.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
PY

echo "🚀 RENDSZER ÉLESÍTVE. Most töltsd ki a .env fájlt a kulcsaiddal!"
python app.py
