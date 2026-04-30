#!/data/data/com.termux/files/usr/bin/bash

DB="titanium_system.db"

echo "======================================"
echo "🔥 TITANIUM FULL CONTROL AUDIT V4"
echo "======================================"

echo ""
echo "📦 1. TABLES"
sqlite3 $DB "SELECT name FROM sqlite_master WHERE type='table';"

echo ""
echo "🧠 2. LEADS SCHEMA"
sqlite3 $DB "PRAGMA table_info(leads);"

echo ""
echo "📊 3. CORE BUSINESS METRICS"
sqlite3 $DB "
SELECT
  COUNT(*) AS total_leads,
  SUM(opt_in) AS opt_in,
  SUM(CASE WHEN opt_in=0 THEN 1 ELSE 0 END) AS blocked,
  SUM(CASE WHEN decision_state='CUSTOMER' THEN 1 ELSE 0 END) AS customers,
  SUM(revenue_value) AS revenue,
  AVG(signal_score) AS avg_signal
FROM leads;
"

echo ""
echo "📈 4. DECISION BREAKDOWN"
sqlite3 $DB "
SELECT decision_state, COUNT(*)
FROM leads
GROUP BY decision_state
ORDER BY COUNT(*) DESC;
"

echo ""
echo "⚙️ 5. ACTION ENGINE STATUS"
sqlite3 $DB "
SELECT action, COUNT(*)
FROM action_queue
GROUP BY action;
"

echo ""
echo "🔥 6. EVENTS + REVENUE"
sqlite3 $DB "
SELECT COUNT(*) AS events FROM events;
SELECT COUNT(*) AS conversions, COALESCE(SUM(amount),0) AS revenue FROM conversions;
"

echo ""
echo "💰 7. SIGNAL QUALITY"
sqlite3 $DB "
SELECT
  AVG(signal_score) AS avg_signal,
  MAX(signal_score) AS max_signal,
  MIN(signal_score) AS min_signal
FROM leads;
"

echo ""
echo "🧾 8. DATA QUALITY"
sqlite3 $DB "
SELECT
  SUM(CASE WHEN email IS NULL OR email='' THEN 1 ELSE 0 END) AS missing_email,
  SUM(CASE WHEN website IS NULL OR website='' THEN 1 ELSE 0 END) AS missing_website
FROM leads;
"

echo ""
echo "⚡ 9. STRIPE WEBHOOK DIAGNOSIS"
echo "CHECK:"
echo "- endpoint must return HTTP 200 < 2s"
echo "- no DB blocking inside webhook"
echo "- async processing required"
echo "- HF space must not sleep/crash"

echo ""
echo "======================================"
echo "✅ AUDIT COMPLETE"
echo "======================================"
