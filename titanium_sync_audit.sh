#!/data/data/com.termux/files/usr/bin/bash

echo "=============================="
echo "🔥 TITANIUM FULL SYNC AUDIT"
echo "Render + HuggingFace + DB"
echo "=============================="

DB="titanium_system.db"

echo ""
echo "1. LOCAL DATABASE STATUS"
echo "------------------------"

sqlite3 $DB "
SELECT 'leads' AS table_name, COUNT(*) FROM leads
UNION ALL
SELECT 'events', COUNT(*) FROM events
UNION ALL
SELECT 'conversions', COUNT(*) FROM conversions
UNION ALL
SELECT 'action_queue', COUNT(*) FROM action_queue;
"

echo ""
echo "2. SIGNAL + REVENUE CHECK"
echo "------------------------"

sqlite3 $DB "
SELECT
  COUNT(*) AS total_leads,
  SUM(revenue_value) AS revenue,
  AVG(signal_score) AS avg_signal
FROM leads;
"

echo ""
echo "3. WEBHOOK LOCAL TEST"
echo "------------------------"

curl -s -o /dev/null -w "Webhook HTTP Status: %{http_code}\n" \
http://127.0.0.1:8080/webhook || echo "Webhook OFFLINE"

echo ""
echo "4. RENDER SYNC CHECK"
echo "------------------------"

RENDER_URL="https://pityumajsaii-titanium.hf.space/webhook"

curl -s -o /dev/null -w "Render Webhook Status: %{http_code}\n" \
$RENDER_URL || echo "Render endpoint unreachable"

echo ""
echo "5. HUGGINGFACE SPACE CHECK"
echo "------------------------"

HF_URL="https://huggingface.co"

curl -s -o /dev/null -w "HF Base Status: %{http_code}\n" \
$HF_URL || echo "HF unreachable"

echo ""
echo "6. SYSTEM HEALTH SUMMARY"
echo "------------------------"

sqlite3 $DB "
SELECT
  decision_state,
  COUNT(*) as cnt
FROM leads
GROUP BY decision_state
ORDER BY cnt DESC;
"

echo ""
echo "7. QUEUE STATUS"
echo "------------------------"

sqlite3 $DB "
SELECT COUNT(*) AS queued_actions FROM action_queue;
"

echo ""
echo "=============================="
echo "DONE - SYNC AUDIT COMPLETE"
echo "=============================="
