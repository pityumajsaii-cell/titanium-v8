import sqlite3

services = [

# SALES
("AI Lead Generation","Sales",299),
("AI Appointment Setter","Sales",399),
("AI CRM Automation","Sales",499),
("AI Cold Email Engine","Sales",699),
("AI Followup System","Sales",399),

# MARKETING
("AI Content Machine","Marketing",499),
("AI YouTube Autoposter","Marketing",699),
("AI TikTok Growth Engine","Marketing",699),
("AI Ad Copy Generator","Marketing",399),
("AI SEO Booster","Marketing",799),

# FINANCE
("AI Invoice Automation","Finance",499),
("AI Bookkeeping Assistant","Finance",699),
("AI Cashflow Predictor","Finance",899),
("AI Tax Reminder Bot","Finance",499),
("AI CFO Dashboard","Finance",1499),

# ENGINEERING
("AI Quote Builder","Engineering",999),
("AI Construction Planner","Engineering",1499),
("AI Maintenance Predictor","Engineering",1299),
("AI CAD Assistant","Engineering",1999),
("AI Safety Monitor","Engineering",1499),

# REAL ESTATE
("AI Property Funnel","Real Estate",999),
("AI Tenant Bot","Real Estate",699),
("AI Rental Manager","Real Estate",899),
("AI Lead Qualifier","Real Estate",799),
("AI Agency Growth OS","Real Estate",1499),

# HEALTHCARE
("AI Booking Clinic","Healthcare",699),
("AI Reminder System","Healthcare",499),
("AI Patient Funnel","Healthcare",999),
("AI Dental Growth Bot","Healthcare",1499),
("AI Reception Assistant","Healthcare",899),

# ECOM
("AI Product Writer","Ecommerce",499),
("AI Cart Recovery","Ecommerce",699),
("AI Customer Chatbot","Ecommerce",799),
("AI Review Collector","Ecommerce",599),
("AI Store Growth OS","Ecommerce",1499),

# SAAS
("AI White Label SaaS","SaaS",1999),
("AI Client Portal","SaaS",1499),
("AI Subscription Engine","SaaS",1299),
("AI Agency OS","SaaS",2499),
("AI Holding OS Enterprise","SaaS",4999),
]

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS services(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
category TEXT,
price INTEGER
)
""")

c.execute("DELETE FROM services")

for s in services:
    c.execute("INSERT INTO services(name,category,price) VALUES(?,?,?)", s)

db.commit()
db.close()

print(f"✅ LOADED {len(services)} SERVICES")
