BEGIN TRANSACTION;

INSERT INTO leads
(created,company,email,city,country,niche,website,status,owner,notes)
VALUES

(datetime('now'),'Miami Elite Roofing','info@miamieliteroofing.com','Miami','USA','Roofing','https://miamieliteroofing.com','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Florida Roof Masters','contact@floridaroofmasters.com','Miami','USA','Roofing','https://floridaroofmasters.com','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Sunrise Roofing Group','sales@sunriseroofinggroup.com','Miami','USA','Roofing','https://sunriseroofinggroup.com','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Dallas Premier Roofing','info@dallaspremierroofing.com','Dallas','USA','Roofing','https://dallaspremierroofing.com','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Texas Star Roofing','contact@texasstarroofing.com','Dallas','USA','Roofing','https://texasstarroofing.com','NEW','TITANIUM','MONEY250'),

(datetime('now'),'Austin Cool Air','info@austincoolair.com','Austin','USA','HVAC','https://austincoolair.com','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Capital HVAC Austin','contact@capitalhvac.com','Austin','USA','HVAC','https://capitalhvac.com','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Phoenix Air Experts','info@phoenixairexperts.com','Phoenix','USA','HVAC','https://phoenixairexperts.com','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Vegas Climate Pros','hello@vegasclimatepros.com','Las Vegas','USA','HVAC','https://vegasclimatepros.com','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Denver Heat Air','info@denverheatair.com','Denver','USA','HVAC','https://denverheatair.com','NEW','TITANIUM','MONEY250'),

(datetime('now'),'Zurich Smile Clinic','info@zurichsmileclinic.ch','Zurich','Switzerland','Dentist','https://zurichsmileclinic.ch','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Swiss Dental Group','contact@swissdentalgroup.ch','Zurich','Switzerland','Dentist','https://swissdentalgroup.ch','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Geneva Wealth Partners','info@genevawealth.ch','Geneva','Switzerland','Finance','https://genevawealth.ch','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Basel Finance Desk','hello@baselfinance.ch','Basel','Switzerland','Finance','https://baselfinance.ch','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Bern Tax Advisory','contact@berntax.ch','Bern','Switzerland','Accounting','https://berntax.ch','NEW','TITANIUM','MONEY250'),

(datetime('now'),'Dubai Prime Realty','info@dubaiprime.ae','Dubai','UAE','Real Estate','https://dubaiprime.ae','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Dubai Elite Homes','sales@dubaihomes.ae','Dubai','UAE','Real Estate','https://dubaihomes.ae','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Palm Dental Dubai','hello@palmdental.ae','Dubai','UAE','Dentist','https://palmdental.ae','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Luxury Med Spa Dubai','info@luxurymedspa.ae','Dubai','UAE','Med Spa','https://luxurymedspa.ae','NEW','TITANIUM','MONEY250'),
(datetime('now'),'Marina Realty Group','contact@marinarealty.ae','Dubai','UAE','Real Estate','https://marinarealty.ae','NEW','TITANIUM','MONEY250');

COMMIT;
