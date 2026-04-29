#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "🏦 TITANIUM MONEY V2 - SWISS DENTIST MODE - DEPLOYING"

# Adatstruktúra az ügyfélkezeléshez
mkdir -p leads/zurich contracts/switzerland invoices/chf

cat > app.py << 'PY'
import os, sqlite3, stripe, requests, threading
from flask import Flask, request, jsonify
from openai import OpenAI
import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# --- ÉLES KONFIGURÁCIÓ ---
stripe.api_key = os.getenv("STRIPE_SECRET")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

DB_PATH = "titanium_v2_money.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS leads (id INTEGER PRIMARY KEY, name TEXT, email TEXT, city TEXT, status TEXT)")
        conn.execute("CREATE TABLE IF NOT EXISTS deals (id INTEGER PRIMARY KEY, lead_id INTEGER, amount REAL, status TEXT)")

# --- 1. REAL-WORLD SCRAPER LOGIKA (ZÜRICH) ---
def get_swiss_leads(city="Zürich"):
    """
    Ez a modul a Google Places API vagy srape logika helyőrzője.
    A Gemini-t itt arra használjuk, hogy a begyűjtött nyers adatokat (pl. weboldal szövege) 
    átalakítsa döntéshozói profilokká.
    """
    search_query = f"Zahnarzt {city} contact email"
    # Itt futna a Requests + BeautifulSoup a valódi scrapinghez
    print(f"🔍 Kutatás indítása: {search_query}...")
    return f"Swiss-Dent-Clinic-{city}", "info@swissdentexample.ch"

# --- 2. HYBRID SALES ENGINE ---
def generate_high_ticket_offer(clinic_name):
    # OpenAI GPT-4o: A pszichológiai hadviselés és a zárás mestere
    offer_prompt = f"""Írj egy német nyelvű, profi üzleti ajánlatot a {clinic_name} részére.
    Ajánlat: '10 neue Patienten in 30 Tagen oder Geld-zurück-Garantie'.
    Fókusz: AI-alapú páciens-szerzés, automatizált visszahívás, Google értékelés növelés.
    Ár: 490 EUR Setup + 790 EUR/hó."""
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "Du bist ein Senior Sales Specialist für Schweizer Zahnärzte."},
                  {"role": "user", "content": offer_prompt}]
    )
    return response.choices[0].message.content

# --- 3. CASHFLOW & SUBSCRIPTION ---
@app.route("/create-subscription", methods=["POST"])
def create_subscription():
    data = request.json # email, clinic_name
    try:
        # 490 EUR Setup + 790 EUR havi díj (Stripe-on beállított termékek kellenek)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email=data['email'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'chf',
                        'product_data': {'name': 'Titanium Dental Setup'},
                        'unit_amount': 49000,
                    },
                    'quantity': 1,
                },
                {
                    'price_data': {
                        'currency': 'chf',
                        'product_data': {'name': 'Monthly Patient Pipeline'},
                        'unit_amount': 79000,
                        'recurring': {'interval': 'month'},
                    },
                    'quantity': 1,
                }
            ],
            mode='subscription',
            success_url="https://titanium-v2.vercel.app/success",
            cancel_url="https://titanium-v2.vercel.app/cancel",
        )
        return jsonify({"checkout_url": session.url})
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=7860)
PY

echo "🚀 TITANIUM V2 ONLINE. Célpont: Zürich. Pénz: CHF/EUR."
python app.py
