BEGIN TRANSACTION;

INSERT INTO leads
(created,company,email,city,country,niche,website,status,owner,notes)
VALUES

-- SWITZERLAND
(datetime('now'),'Zurich Smile Experts','info@zurichsmileexperts.ch','Zurich','Switzerland','Dentist','https://zurichsmileexperts.ch','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Geneva Wealth Office','contact@genevawealthoffice.ch','Geneva','Switzerland','Finance','https://genevawealthoffice.ch','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Basel Tax Partners','sales@baseltaxpartners.ch','Basel','Switzerland','Accounting','https://baseltaxpartners.ch','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Bern Private Finance','info@bernprivatefinance.ch','Bern','Switzerland','Finance','https://bernprivatefinance.ch','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Lucerne Dental Care','hello@lucernedentalcare.ch','Lucerne','Switzerland','Dentist','https://lucernedentalcare.ch','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Lausanne Advisors','info@lausanneadvisors.ch','Lausanne','Switzerland','Finance','https://lausanneadvisors.ch','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Winterthur Smile Group','contact@winterthursmile.ch','Winterthur','Switzerland','Dentist','https://winterthursmile.ch','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'St Gallen Tax House','sales@stgallentax.ch','St Gallen','Switzerland','Accounting','https://stgallentax.ch','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Lugano Finance Hub','info@luganofinance.ch','Lugano','Switzerland','Finance','https://luganofinance.ch','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Fribourg Dental Studio','hello@fribourgdental.ch','Fribourg','Switzerland','Dentist','https://fribourgdental.ch','NEW','TITANIUM','SWISS_AUS_BATCH'),

-- AUSTRALIA
(datetime('now'),'Sydney Smile Clinic','info@sydneysmileclinic.au','Sydney','Australia','Dentist','https://sydneysmileclinic.au','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Melbourne Roofing Co','contact@melbourneroofing.au','Melbourne','Australia','Roofing','https://melbourneroofing.au','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Brisbane Air Systems','sales@brisbaneairsystems.au','Brisbane','Australia','HVAC','https://brisbaneairsystems.au','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Perth Finance Group','info@perthfinance.au','Perth','Australia','Finance','https://perthfinance.au','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Adelaide Tax Partners','hello@adelaidetax.au','Adelaide','Australia','Accounting','https://adelaidetax.au','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Gold Coast Dental Hub','info@gcdentalhub.au','Gold Coast','Australia','Dentist','https://gcdentalhub.au','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Canberra Wealth Office','contact@canberrawealth.au','Canberra','Australia','Finance','https://canberrawealth.au','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Newcastle Cool Air','sales@newcastlecoolair.au','Newcastle','Australia','HVAC','https://newcastlecoolair.au','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Hobart Roofing Experts','info@hobartroofing.au','Hobart','Australia','Roofing','https://hobartroofing.au','NEW','TITANIUM','SWISS_AUS_BATCH'),
(datetime('now'),'Sunshine Coast Smile','hello@sunshinecoastsmile.au','Sunshine Coast','Australia','Dentist','https://sunshinecoastsmile.au','NEW','TITANIUM','SWISS_AUS_BATCH');

COMMIT;
