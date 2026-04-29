BEGIN TRANSACTION;

INSERT INTO leads
(created,company,email,city,country,niche,website,status,owner,notes)
VALUES

(datetime('now'),'Houston Roof Experts','info@houstonroofexperts.com','Houston','USA','Roofing','https://houstonroofexperts.com','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Atlanta Roofing Hub','contact@atlantaroofinghub.com','Atlanta','USA','Roofing','https://atlantaroofinghub.com','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Chicago Top Roofing','sales@chicagotoproofing.com','Chicago','USA','Roofing','https://chicagotoproofing.com','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Seattle Roof Repair','info@seattleroofrepair.com','Seattle','USA','Roofing','https://seattleroofrepair.com','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Orlando Roofing Team','hello@orlandoroofingteam.com','Orlando','USA','Roofing','https://orlandoroofingteam.com','NEW','TITANIUM','MONEY250_P2'),

(datetime('now'),'Houston AC Masters','info@houstonacmasters.com','Houston','USA','HVAC','https://houstonacmasters.com','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Chicago Climate Pros','contact@chicagoclimatepros.com','Chicago','USA','HVAC','https://chicagoclimatepros.com','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Seattle Air Comfort','sales@seattleaircomfort.com','Seattle','USA','HVAC','https://seattleaircomfort.com','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Atlanta Cool Systems','info@atlcoolsystems.com','Atlanta','USA','HVAC','https://atlcoolsystems.com','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Orlando Breeze HVAC','hello@orlandobreezehvac.com','Orlando','USA','HVAC','https://orlandobreezehvac.com','NEW','TITANIUM','MONEY250_P2'),

(datetime('now'),'Zurich Tax House','info@zurichtaxhouse.ch','Zurich','Switzerland','Accounting','https://zurichtaxhouse.ch','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Geneva Private Finance','contact@genevaprivatefinance.ch','Geneva','Switzerland','Finance','https://genevaprivatefinance.ch','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Basel Smile Center','hello@baselsmilecenter.ch','Basel','Switzerland','Dentist','https://baselsmilecenter.ch','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Bern Dental Care','info@berndentalcare.ch','Bern','Switzerland','Dentist','https://berndentalcare.ch','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Lucerne Wealth Group','sales@lucernewealth.ch','Lucerne','Switzerland','Finance','https://lucernewealth.ch','NEW','TITANIUM','MONEY250_P2'),

(datetime('now'),'Dubai Marina Realty','info@dubaimarinarealty.ae','Dubai','UAE','Real Estate','https://dubaimarinarealty.ae','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Burj Property Advisors','contact@burjproperty.ae','Dubai','UAE','Real Estate','https://burjproperty.ae','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Jumeirah Dental Studio','hello@jumeirahdental.ae','Dubai','UAE','Dentist','https://jumeirahdental.ae','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Dubai Skin Med Spa','info@dubaiskinspa.ae','Dubai','UAE','Med Spa','https://dubaiskinspa.ae','NEW','TITANIUM','MONEY250_P2'),
(datetime('now'),'Emirates Luxury Realty','sales@emiratesluxuryrealty.ae','Dubai','UAE','Real Estate','https://emiratesluxuryrealty.ae','NEW','TITANIUM','MONEY250_P2');

COMMIT;
