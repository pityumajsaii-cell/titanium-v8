import sqlite3

demo = [
("John Smith","john@company1.com","Company One","AI Lead Generation"),
("Anna White","anna@clinic.com","Dental Clinic","AI Booking Bot"),
("Mark Lee","mark@agency.com","Growth Agency","AI CRM Automation"),
("David Fox","david@shop.com","Ecommerce Store","AI Sales Bot"),
("Julia Kent","julia@estate.com","Real Estate Pro","AI Funnel System")
]

db=sqlite3.connect("data/titanium.db")
c=db.cursor()

count=0
for d in demo:
    c.execute("""
    INSERT INTO leads(name,email,company,service,status)
    VALUES(?,?,?,?, 'new')
    """, d)
    count+=1

db.commit()
db.close()

print(f"🎯 NEW LEADS ADDED: {count}")
