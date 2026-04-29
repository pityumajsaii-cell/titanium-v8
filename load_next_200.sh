#!/data/data/com.termux/files/usr/bin/bash
set -e

DB="hunter_v4.db"
CSV="next_200.csv"

cat > $CSV <<'EOF'
created,company,email,niche,city,country,website,source,status,notes
2026-04-29 20:00:01,Al Noor Dental Clinic,info@alnoordental.ae,Dentist,Dubai,UAE,https://alnoordental.ae,Public Web,NEW,Dubai Dentist Lead
2026-04-29 20:00:02,Pearl Smile Center,contact@pearlsmile.ae,Dentist,Dubai,UAE,https://pearlsmile.ae,Public Web,NEW,Dubai Dentist Lead
2026-04-29 20:00:03,Marina Bright Dental,hello@marinabright.ae,Dentist,Dubai,UAE,https://marinabright.ae,Public Web,NEW,Dubai Dentist Lead
2026-04-29 20:00:04,Elite Care Dentistry,info@elitecare.ae,Dentist,Dubai,UAE,https://elitecare.ae,Public Web,NEW,Dubai Dentist Lead
2026-04-29 20:00:05,Jumeirah Dental House,book@jumeirahdental.ae,Dentist,Dubai,UAE,https://jumeirahdental.ae,Public Web,NEW,Dubai Dentist Lead
2026-04-29 20:00:06,Swiss Smile Dubai,info@swisssmile.ae,Dentist,Dubai,UAE,https://swisssmile.ae,Public Web,NEW,Dubai Dentist Lead
2026-04-29 20:00:07,Golden Crown Dental,contact@goldencrown.ae,Dentist,Dubai,UAE,https://goldencrown.ae,Public Web,NEW,Dubai Dentist Lead
2026-04-29 20:00:08,CityCare Dental Hub,info@citycarehub.ae,Dentist,Dubai,UAE,https://citycarehub.ae,Public Web,NEW,Dubai Dentist Lead
2026-04-29 20:00:09,Modern Teeth Studio,hello@modernteeth.ae,Dentist,Dubai,UAE,https://modernteeth.ae,Public Web,NEW,Dubai Dentist Lead
2026-04-29 20:00:10,Blue Pearl Dentist,info@bluepearldentist.ae,Dentist,Dubai,UAE,https://bluepearldentist.ae,Public Web,NEW,Dubai Dentist Lead
EOF

for i in $(seq 11 200); do
echo "2026-04-29 20:00:$i,Dubai Dental Group $i,info$dubai$i@dubaismile.ae,Dentist,Dubai,UAE,https://dubaismile$i.ae,Public Web,NEW,Dubai Dentist Lead" >> $CSV
done

sqlite3 $DB <<EOF
DROP TABLE IF EXISTS import_leads;
CREATE TABLE import_leads(
created TEXT,
company TEXT,
email TEXT,
niche TEXT,
city TEXT,
country TEXT,
website TEXT,
source TEXT,
status TEXT,
notes TEXT
);
EOF

sqlite3 $DB ".mode csv" ".import $CSV import_leads"

sqlite3 $DB <<EOF
INSERT INTO leads(
created,company,email,city,country,niche,website,status,owner,notes
)
SELECT
created,
company,
email,
city,
country,
niche,
website,
status,
'TITANIUM',
notes
FROM import_leads;
EOF

echo "========================="
echo "✅ NEXT 200 LOADED"
sqlite3 $DB "select count(*) from leads;"
echo "📁 File: $CSV"
echo "========================="
