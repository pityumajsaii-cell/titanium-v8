import sqlite3

services = [
("AI Lead Generation","Sales",299,"Lead generation system"),
("AI Booking Bot","Sales",499,"Appointment booking bot"),
("AI Accounting Assistant","Finance",699,"Invoice/admin automation"),
("AI Marketing Engine","Marketing",999,"Content + ads system"),
("AI Logistics Planner","Operations",1499,"Fleet/route automation"),
("AI Engineering Estimator","Engineering",1999,"Quote automation"),
("AI SaaS White Label","SaaS",2499,"Rentable AI software")
]

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

for s in services:
    c.execute("INSERT INTO services(name,category,price,description) VALUES(?,?,?,?)", s)

db.commit()
db.close()

print("✅ SERVICES LOADED")
