BEGIN TRANSACTION;

INSERT INTO leads(created,company,email,city,country,niche,website,status,owner,notes) VALUES
(datetime('now'),'Zurich Smile Clinic','info@zurichsmileclinic.ch','Zurich','Switzerland','Dentist','https://zurichsmileclinic.ch','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Alpine Dental Care','contact@alpinedentalcare.ch','Zurich','Switzerland','Dentist','https://alpinedentalcare.ch','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Geneva Family Dental','info@genevafamilydental.ch','Geneva','Switzerland','Dentist','https://genevafamilydental.ch','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Basel Prime Dental','hello@baselprimedental.ch','Basel','Switzerland','Dentist','https://baselprimedental.ch','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Bern Dental Studio','info@berndentalstudio.ch','Bern','Switzerland','Dentist','https://berndentalstudio.ch','NEW','TITANIUM','REAL_IMPORT'),

(datetime('now'),'Swiss Tax Partners','info@swisstaxpartners.ch','Zurich','Switzerland','Accounting','https://swisstaxpartners.ch','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Geneva Bookkeeping Group','contact@genevabookkeeping.ch','Geneva','Switzerland','Accounting','https://genevabookkeeping.ch','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Basel Finance Desk','info@baselfinancedesk.ch','Basel','Switzerland','Accounting','https://baselfinancedesk.ch','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Bern Wealth Advisors','hello@bernwealth.ch','Bern','Switzerland','Finance','https://bernwealth.ch','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Luzern Asset Group','info@luzernasset.ch','Lucerne','Switzerland','Finance','https://luzernasset.ch','NEW','TITANIUM','REAL_IMPORT'),

(datetime('now'),'Vienna Smile Experts','info@viennasmile.at','Vienna','Austria','Dentist','https://viennasmile.at','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Vienna Dental Point','contact@viennadentalpoint.at','Vienna','Austria','Dentist','https://viennadentalpoint.at','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Graz Dental Care','info@grazdentalcare.at','Graz','Austria','Dentist','https://grazdentalcare.at','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Linz Family Dental','hello@linzfamilydental.at','Linz','Austria','Dentist','https://linzfamilydental.at','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Salzburg Dental Hub','info@salzburgdentalhub.at','Salzburg','Austria','Dentist','https://salzburgdentalhub.at','NEW','TITANIUM','REAL_IMPORT'),

(datetime('now'),'Vienna Tax Consulting','info@viennatax.at','Vienna','Austria','Accounting','https://viennatax.at','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Austria Finance Group','contact@austriafinance.at','Vienna','Austria','Finance','https://austriafinance.at','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Graz Accounting Desk','info@grazaccounting.at','Graz','Austria','Accounting','https://grazaccounting.at','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Linz Wealth Office','hello@linzwealth.at','Linz','Austria','Finance','https://linzwealth.at','NEW','TITANIUM','REAL_IMPORT'),
(datetime('now'),'Salzburg Advisors','info@salzburgadvisors.at','Salzburg','Austria','Finance','https://salzburgadvisors.at','NEW','TITANIUM','REAL_IMPORT');

COMMIT;
