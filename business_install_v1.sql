BEGIN;

-- =========================================================
-- 1. CUSTOMERS (alap üzleti entitás)
-- =========================================================

CREATE TABLE IF NOT EXISTS customers (
  id INTEGER PRIMARY KEY,
  email TEXT UNIQUE,
  name TEXT,
  country TEXT,
  opt_in INTEGER DEFAULT 1,
  lifetime_value REAL DEFAULT 0,
  segment TEXT DEFAULT 'NEW',
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================================================
-- 2. PRODUCTS (termék / szolgáltatás katalógus)
-- =========================================================

CREATE TABLE IF NOT EXISTS products (
  id INTEGER PRIMARY KEY,
  name TEXT,
  description TEXT,
  price REAL,
  currency TEXT DEFAULT 'EUR',
  active INTEGER DEFAULT 1,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================================================
-- 3. ORDERS (vásárlási esemény)
-- =========================================================

CREATE TABLE IF NOT EXISTS orders (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  product_id INTEGER,
  amount REAL,
  status TEXT DEFAULT 'PENDING', -- PENDING / PAID / FAILED / REFUNDED
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================================================
-- 4. PAYMENTS (Stripe mirror layer)
-- =========================================================

CREATE TABLE IF NOT EXISTS payments (
  id INTEGER PRIMARY KEY,
  order_id INTEGER,
  stripe_payment_intent TEXT,
  stripe_charge_id TEXT,
  amount REAL,
  currency TEXT DEFAULT 'EUR',
  status TEXT DEFAULT 'PENDING',
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================================================
-- 5. SUBSCRIPTIONS (Stripe subscription layer)
-- =========================================================

CREATE TABLE IF NOT EXISTS subscriptions (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  stripe_subscription_id TEXT,
  plan TEXT,
  status TEXT DEFAULT 'ACTIVE',
  current_period_end TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================================================
-- 6. EVENTS (viselkedés + tracking)
-- =========================================================

CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  event_type TEXT, -- view / click / purchase / login
  value REAL DEFAULT 0,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================================================
-- 7. REVENUE LEDGER (valódi pénz igazság réteg)
-- =========================================================

CREATE TABLE IF NOT EXISTS revenue_ledger (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  source TEXT, -- stripe / manual / affiliate
  amount REAL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================================================
-- 8. ACTION QUEUE (sales automation motor)
-- =========================================================

CREATE TABLE IF NOT EXISTS action_queue (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  action TEXT,
  status TEXT DEFAULT 'PENDING',
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================================================
-- 9. REVENUE SYNC (Stripe → ledger)
-- =========================================================

INSERT INTO revenue_ledger (customer_id, source, amount)
SELECT
  o.customer_id,
  'stripe',
  p.amount
FROM payments p
JOIN orders o ON o.id = p.order_id
WHERE p.status = 'succeeded';

-- =========================================================
-- 10. CUSTOMER LIFETIME VALUE
-- =========================================================

UPDATE customers
SET lifetime_value = (
  SELECT COALESCE(SUM(amount),0)
  FROM revenue_ledger
  WHERE revenue_ledger.customer_id = customers.id
);

-- =========================================================
-- 11. SEGMENTATION ENGINE
-- =========================================================

UPDATE customers
SET segment =
CASE
  WHEN lifetime_value > 500 THEN 'VIP'
  WHEN lifetime_value > 100 THEN 'ACTIVE'
  WHEN lifetime_value > 0 THEN 'PAYING'
  ELSE 'FREE'
END;

-- =========================================================
-- 12. ACTION ENGINE (AUTOMATION OUTPUT)
-- =========================================================

DELETE FROM action_queue;

INSERT INTO action_queue (customer_id, action)
SELECT id,
CASE
  WHEN segment='VIP' THEN 'HIGH_VALUE_UPSELL'
  WHEN segment='ACTIVE' THEN 'CROSS_SELL'
  WHEN segment='PAYING' THEN 'NURTURE'
  ELSE 'ACQUIRE'
END
FROM customers;

-- =========================================================
-- 13. BUSINESS HEALTH DASHBOARD
-- =========================================================

SELECT
  COUNT(*) AS customers,
  SUM(lifetime_value) AS revenue,
  AVG(lifetime_value) AS avg_customer_value
FROM customers;

SELECT segment, COUNT(*) FROM customers GROUP BY segment;

COMMIT;
