BEGIN TRANSACTION;

INSERT INTO leads
(created,company,email,city,country,niche,website,status,owner,notes)
VALUES

(datetime('now'),'Boston Roofing Pros','info@bostonroofingpros.com','Boston','USA','Roofing','https://bostonroofingpros.com','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'San Diego Roof Works','contact@sandiegoroofworks.com','San Diego','USA','Roofing','https://sandiegoroofworks.com','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Charlotte Roofing Group','sales@charlotteroofinggroup.com','Charlotte','USA','Roofing','https://charlotteroofinggroup.com','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Nashville Roof Masters','info@nashvilleroofmasters.com','Nashville','USA','Roofing','https://nashvilleroofmasters.com','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Tampa Roofing Experts','hello@tamparoofingexperts.com','Tampa','USA','Roofing','https://tamparoofingexperts.com','NEW','TITANIUM','MONEY250_P3'),

(datetime('now'),'Boston Climate Control','info@bostonclimatecontrol.com','Boston','USA','HVAC','https://bostonclimatecontrol.com','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'San Diego Air Masters','contact@sdairmasters.com','San Diego','USA','HVAC','https://sdairmasters.com','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Charlotte Comfort HVAC','sales@charlottecomforthvac.com','Charlotte','USA','HVAC','https://charlottecomforthvac.com','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Nashville Cool Air','info@nashvillecoolair.com','Nashville','USA','HVAC','https://nashvillecoolair.com','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Tampa Air Systems','hello@tampaairsystems.com','Tampa','USA','HVAC','https://tampaairsystems.com','NEW','TITANIUM','MONEY250_P3'),

(datetime('now'),'Zurich Elite Dental','info@zurichelitedental.ch','Zurich','Switzerland','Dentist','https://zurichelitedental.ch','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Geneva Tax Group','contact@genevataxgroup.ch','Geneva','Switzerland','Accounting','https://genevataxgroup.ch','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Basel Wealth Office','sales@baselwealthoffice.ch','Basel','Switzerland','Finance','https://baselwealthoffice.ch','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Bern Smile Studio','info@bernsmilestudio.ch','Bern','Switzerland','Dentist','https://bernsmilestudio.ch','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Lausanne Finance Hub','hello@lausannefinancehub.ch','Lausanne','Switzerland','Finance','https://lausannefinancehub.ch','NEW','TITANIUM','MONEY250_P3'),

(datetime('now'),'Dubai Harbor Realty','info@dubaiharborrealty.ae','Dubai','UAE','Real Estate','https://dubaiharborrealty.ae','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Skyline Property Dubai','contact@skylinepropertydubai.ae','Dubai','UAE','Real Estate','https://skylinepropertydubai.ae','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Palm Smile Dental','sales@palmsmiledental.ae','Dubai','UAE','Dentist','https://palmsmiledental.ae','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Elite Beauty Med Spa','info@elitebeautymedspa.ae','Dubai','UAE','Med Spa','https://elitebeautymedspa.ae','NEW','TITANIUM','MONEY250_P3'),
(datetime('now'),'Golden Sands Realty','hello@goldensandsrealty.ae','Dubai','UAE','Real Estate','https://goldensandsrealty.ae','NEW','TITANIUM','MONEY250_P3');

COMMIT;
