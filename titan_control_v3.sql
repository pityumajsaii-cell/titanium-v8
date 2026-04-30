BEGIN;

-- =========================
-- USERS / CUSTOMERS
-- =========================

CREATE TABLE IF NOT EXISTS customers (
  id INTEGER PRIMARY KEY,
  email TEXT UNIQUE,
  name TEXT,
  country TEXT,
  opt_in INTEGER DEFAULT 1,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- PRODUCTS / SERVICES
-- =========================

CREATE TABLE IF NOT EXISTS products (
  id INTEGER PRIMARY KEY,
  name TEXT,
  description TEXT,
  price REAL,
  currency TEXT DEFAULT 'EUR',
  active INTEGER DEFAULT 1,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- ORDERS (BUSINESS CORE)
-- =========================

CREATE TABLE IF NOT EXISTS orders (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  product_id INTEGER,
  amount REAL,
  status TEXT DEFAULT 'PENDING',  -- pending / paid / failed / refunded
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- PAYMENTS (STRIPE MIRROR)
-- =========================

CREATE TABLE IF NOT EXISTS payments (
  id INTEGER PRIMARY KEY,
  order_id INTEGER,
  stripe_payment_intent TEXT,
  stripe_charge_id TEXT,
  amount REAL,
  currency TEXT,
  status TEXT, -- succeeded / pending / failed
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- SUBSCRIPTIONS (STRIPE CORE)
-- =========================

CREATE TABLE IF NOT EXISTS subscriptions (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  stripe_subscription_id TEXT,
  plan TEXT,
  status TEXT, -- active / canceled / past_due
  current_period_end TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- EVENTS (TRACKING / ANALYTICS)
-- =========================

CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  event_type TEXT, -- view / click / purchase / login
  value REAL DEFAULT 0,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- REVENUE LEDGER (TRUTH SOURCE)
-- =========================

CREATE TABLE IF NOT EXISTS revenue_ledger (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  source TEXT, -- stripe / manual / affiliate
  amount REAL,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

COMMIT;
