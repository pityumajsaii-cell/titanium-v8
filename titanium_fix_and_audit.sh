#!/data/data/com.termux/files/usr/bin/bash

DB="titanium_system.db"

echo "===================================="
echo "🔥 TITANIUM FULL FIX + AUDIT (STABLE)"
echo "===================================="

# -------------------------
# 1. DB FIX
# -------------------------
echo "[1] DB integrity fix..."

sqlite3 $DB "
UPDATE leads SET signal_score = COALESCE(signal_score,0);
UPDATE leads SET revenue_value = COALESCE(revenue_value,0);
UPDATE leads SET decision_state = COALESCE(decision_state,'COLD');
"

# -------------------------
# 2. ACTION QUEUE REBUILD
# -------------------------
echo "[2] Rebuilding action queue..."

sqlite3 $DB "
DELETE FROM action_queue;

INSERT INTO action_queue (lead_id, action)
SELECT id,
CASE
  WHEN decision_state='CUSTOMER' THEN 'UPSELL'
  WHEN decision_state='HOT' THEN 'SEND_OFFER'
  WHEN decision_state='COLD' THEN 'NURTURE'
  ELSE 'SUPPRESS'
END
FROM leads;
"

# -------------------------
# 3. HEALTH CHECK
# -------------------------
echo "[3] System health..."

sqlite3 $DB "
SELECT 'leads' AS name, COUNT(*) FROM leads
UNION ALL
SELECT 'events', COUNT(*) FROM events
UNION ALL
SELECT 'queue', COUNT(*) FROM action_queue
UNION ALL
SELECT 'conversions', COUNT(*) FROM conversions;
"

# -------------------------
# 4. REVENUE
# -------------------------
echo "[4] Revenue..."

sqlite3 $DB "
SELECT
COUNT(*) AS conversions,
COALESCE(SUM(amount),0) AS revenue
FROM conversions;
"

# -------------------------
# 5. SIGNALS
# -------------------------
echo "[5] Signals..."

sqlite3 $DB "
SELECT
AVG(signal_score),
MAX(signal_score),
MIN(signal_score)
FROM leads;
"

# -------------------------
# 6. WEBHOOK CHECK
# -------------------------
echo "[6] Webhook check..."

echo "- Must return 200 < 1s"
echo "- Must be async"
echo "- Must verify Stripe signature"

# -------------------------
# 7. RENDER TEST
# -------------------------
echo "[7] Render endpoint..."

curl -s -o /dev/null -w "HTTP: %{http_code}\n" \
https://pityumajsaii-titanium.hf.space/webhook

echo "===================================="
echo "🔥 DONE"
echo "===================================="
