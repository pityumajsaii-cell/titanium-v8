BEGIN TRANSACTION;

INSERT INTO leads
(created,company,email,city,country,niche,website,status,owner,notes)
VALUES

(datetime('now'),'Detroit Roofing Team','info@detroitroofingteam.com','Detroit','USA','Roofing','https://detroitroofingteam.com','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Portland Roof Experts','contact@portlandroofexperts.com','Portland','USA','Roofing','https://portlandroofexperts.com','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Kansas City Roofing','sales@kcroofingpros.com','Kansas City','USA','Roofing','https://kcroofingpros.com','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Cleveland Roof Works','info@clevelandroofworks.com','Cleveland','USA','Roofing','https://clevelandroofworks.com','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Raleigh Roof Masters','hello@raleighroofmasters.com','Raleigh','USA','Roofing','https://raleighroofmasters.com','NEW','TITANIUM','MONEY250_P4'),

(datetime('now'),'Detroit HVAC Pros','info@detroithvacpros.com','Detroit','USA','HVAC','https://detroithvacpros.com','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Portland Air Comfort','contact@portlandaircomfort.com','Portland','USA','HVAC','https://portlandaircomfort.com','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'KC Climate Systems','sales@kcclimatesystems.com','Kansas City','USA','HVAC','https://kcclimatesystems.com','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Cleveland Cool Air','info@clevelandcoolair.com','Cleveland','USA','HVAC','https://clevelandcoolair.com','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Raleigh Breeze HVAC','hello@raleighbreezehvac.com','Raleigh','USA','HVAC','https://raleighbreezehvac.com','NEW','TITANIUM','MONEY250_P4'),

(datetime('now'),'Zurich Finance Experts','info@zurichfinanceexperts.ch','Zurich','Switzerland','Finance','https://zurichfinanceexperts.ch','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Geneva Dental House','contact@genevadentalhouse.ch','Geneva','Switzerland','Dentist','https://genevadentalhouse.ch','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Basel Tax Consulting','sales@baseltaxconsulting.ch','Basel','Switzerland','Accounting','https://baseltaxconsulting.ch','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Bern Wealth Advisors','info@bernwealthadvisors.ch','Bern','Switzerland','Finance','https://bernwealthadvisors.ch','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Lucerne Smile Clinic','hello@lucernesmileclinic.ch','Lucerne','Switzerland','Dentist','https://lucernesmileclinic.ch','NEW','TITANIUM','MONEY250_P4'),

(datetime('now'),'Dubai Crown Realty','info@dubaicrownrealty.ae','Dubai','UAE','Real Estate','https://dubaicrownrealty.ae','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Pearl Homes Dubai','contact@pearlhomesdubai.ae','Dubai','UAE','Real Estate','https://pearlhomesdubai.ae','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Royal Dental Dubai','sales@royaldentaldubai.ae','Dubai','UAE','Dentist','https://royaldentaldubai.ae','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Prestige Med Spa Dubai','info@prestigemedspa.ae','Dubai','UAE','Med Spa','https://prestigemedspa.ae','NEW','TITANIUM','MONEY250_P4'),
(datetime('now'),'Blue Ocean Realty UAE','hello@blueoceanrealty.ae','Dubai','UAE','Real Estate','https://blueoceanrealty.ae','NEW','TITANIUM','MONEY250_P4');

COMMIT;
