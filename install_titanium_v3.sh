#!/data/data/com.termux/files/usr/bin/bash

DB="titanium_system.db"

echo "🔥 TITANIUM CONTROL LAYER V3 INSTALL START"

sqlite3 $DB <<'EOF'

BEGIN;

-- =========================
-- 1. CORE TABLES
-- =========================

CREATE TABLE IF NOT EXISTS leads (
  id INTEGER PRIMARY KEY,
  email TEXT,
  website TEXT,
  opt_in INTEGER DEFAULT 1,
  signal_score REAL DEFAULT 0,
  revenue_value REAL DEFAULT 0,
  decision_state TEXT DEFAULT 'NEW'
);

CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY,
  lead_id INTEGER,
  event_type TEXT,
  value REAL DEFAULT 0,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS conversions (
  id INTEGER PRIMARY KEY,
  lead_id INTEGER,
  amount REAL DEFAULT 0,
  source TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS action_queue (
  id INTEGER PRIMARY KEY,
  lead_id INTEGER,
  action TEXT,
  status TEXT DEFAULT 'PENDING',
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- 2. SEED DATA (IMPORTANT)
-- =========================

INSERT INTO leads (email, website, opt_in)
VALUES
('test1@demo.com','site.com',1),
('test2@demo.com','site.com',1),
('test3@demo.com','site.com',0);

INSERT INTO events (lead_id, event_type, value)
SELECT id,'init',1 FROM leads;

INSERT INTO conversions (lead_id, amount, source)
VALUES (1, 10, 'seed');

-- =========================
-- 3. SIGNAL ENGINE
-- =========================

UPDATE leads
SET signal_score =
  (SELECT COUNT(*)*10 FROM events WHERE events.lead_id = leads.id)
  + CASE WHEN email IS NOT NULL AND email != '' THEN 20 ELSE 0 END
  + CASE WHEN website IS NOT NULL AND website != '' THEN 10 ELSE 0 END;

-- =========================
-- 4. REVENUE ENGINE
-- =========================

UPDATE leads
SET revenue_value =
  (SELECT COALESCE(SUM(amount),0)
   FROM conversions
   WHERE conversions.lead_id = leads.id);

-- =========================
-- 5. DECISION ENGINE
-- =========================

UPDATE leads
SET decision_state =
CASE
  WHEN opt_in=0 THEN 'BLOCKED'
  WHEN revenue_value > 0 THEN 'CUSTOMER'
  WHEN signal_score > 80 THEN 'HOT'
  WHEN signal_score > 50 THEN 'WARM'
  WHEN signal_score > 20 THEN 'COLD'
  ELSE 'DROP'
END;

-- =========================
-- 6. ACTION ENGINE
-- =========================

DELETE FROM action_queue;

INSERT INTO action_queue (lead_id, action)
SELECT id,
CASE
  WHEN decision_state='CUSTOMER' THEN 'UPSELL'
  WHEN decision_state='HOT' THEN 'CLOSE'
  WHEN decision_state='WARM' THEN 'FOLLOW_UP'
  WHEN decision_state='COLD' THEN 'NURTURE'
  WHEN decision_state='BLOCKED' THEN 'SUPPRESS'
  ELSE 'IGNORE'
END
FROM leads;

COMMIT;

-- =========================
-- 7. HEALTH CHECK
-- =========================

SELECT decision_state, COUNT(*) FROM leads GROUP BY decision_state;

SELECT
  COUNT(*) AS total,
  SUM(revenue_value) AS revenue,
  AVG(signal_score) AS avg_signal
FROM leads;

EOF

echo "✅ INSTALL DONE"
echo "🔥 SYSTEM READY (CONTROL LAYER V3 ACTIVE)"
