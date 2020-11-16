/*
SQL-Datei mit folgenden 4 SQL-Queries, wobei vor jeder Anfrage (Query) ein Kommentar steht mit präziser Beschreibung was die Query macht (Datei 5_queries.sql):

1.1. Eine Query mit DISTINCT.
1.2. Eine Query, die einen JOIN über drei oder mehr Tabellen enthält (bitte als "New Style"-JOIN mit "JOIN ... ON").
1.3. Eine Query mit einer Unterabfrage mit Angabe, ob diese Query korreliert ist oder unkorreliert.
1.4. Eine Query, die eines der vier folgenden Statements enthält (gegebenenfalls mit NOT davor): ANY, IN, EXISTS oder ALL.
*/



-- Distinct:

SELECT count(DISTINCT ort) AS "Anzahl Veranstaltungsorte" FROM tournament;

-- Join:

SELECT spieler.vorname AS "Vorname", spieler.nachname AS "Nachname", tournament.id AS "Tournament Nr.", tournament.ort AS "Austragungsort" FROM spieler JOIN profi ON profi.spielerid = spieler.id JOIN tournament ON profi.tournament = tournament.id LIMIT 20; 

-- Uncorrelated Subquery

SELECT vorname, nachname, gewinn FROM spieler WHERE gewinn > (SELECT AVG(gewinn) FROM spieler WHERE aktiv = true) LIMIT 20;

-- Statement:

SELECT vorname, nachname FROM spieler s WHERE EXISTS (SELECT * FROM profi WHERE spielerid = s.id) LIMIT 20;

/*
2.1 Common Table Expressions/WITH-Statements:
Schreiben Sie zunächst eine Anfrage mit einer unkorrelierten Unterabfrage und dokumentieren Sie diese (einfacher Kommentar vor dem SQL).
Formen Sie dann diese Subquery um in eine Common Table Expression.
Ihre Abgabe muss sowohl die Query mit unkorrelierten Unterabfrage (vor der Umformung) als auch die Query mit Common Table Expression enthalten.
2.2 GROUP-BY und Window-Funktionen:
Schreiben Sie eine sinnvolle Query mit einer GROUP BY-Klausel.
Schreiben Sie eine sinnvolle Query mit einer Window-Funktion.
*/

-- Uncorrelated Subquery

SELECT vorname, nachname, gewinn FROM spieler JOIN beginner ON spieler.id = beginner.spielerid WHERE gewinn > (SELECT AVG(gewinn) FROM spieler) LIMIT 20;

--  Converted to Common Table Expression:
WITH 
aboveAverage AS
(SELECT id, vorname, nachname, gewinn FROM spieler WHERE gewinn > (SELECT AVG(gewinn) FROM spieler)),
allBeginner AS
(SELECT spieler.id FROM spieler JOIN beginner ON spieler.id = beginner.spielerid)
SELECT aboveAverage.vorname, aboveAverage.nachname, aboveAverage.gewinn FROM aboveAverage JOIN allBeginner ON aboveAverage.id = allBeginner.id LIMIT 20;


-- 2.2 GROUP-BY und Window-Funktion:

--GROUP-BY:

SELECT ort AS "Veranstaltungs Ort", COUNT(*) AS "Anzahl Turniere" FROM tournament GROUP BY ort LIMIT 20;


-- Window Function: 

SELECT vorname AS "Vorname", nachname AS "Nachname", gewinn AS "Gewinn", gewinn - lead(gewinn,1,gewinn) OVER (ORDER BY gewinn) AS "Vergleich" FROM spieler ORDER BY 3 DESC LIMIT 20;


/*
3.1 Views:
Schreiben Sie eine View, die mindestens drei Tabellen umfasst.
Schreiben Sie dann eine normale Query, welche diese View verwendet.
3.2 Schreiben Sie eine zweite View (also eine "einfachere" View), die sich updaten lässt. Testen Sie, dass die View sich wirklich updaten lässt, wie folgt:
View schreiben (Tipp: Beschränkungen von PostgreSQL beachten, so dass die View "updateable" ist).
Eine Änderung eines bestimmten Datensatzes über diese View schreiben mittels UPDATE (UPDATE <Ihre View> SET ... WHERE ...;).
*/

-- 3.1
CREATE VIEW Teilnehmer AS SELECT spieler.vorname AS "Vorname", spieler.nachname AS "Nachname", tournament.id AS "Tournament Nr.", tournament.ort AS "Austragungsort" FROM spieler JOIN profi ON profi.spielerid = spieler.id JOIN tournament ON profi.tournament = tournament.id;
SELECT * FROM Teilnehmer LIMIT 20;

--3.2
CREATE VIEW ChipLeader AS SELECT vorname, nachname, chipzahl FROM spieler ORDER BY chipzahl DESC; -- Create View
SELECT vorname, chipzahl FROM ChipLeader WHERE vorname LIKE 'Bryn'; -- Check current Chip Count
UPDATE ChipLeader SET chipzahl = 10 WHERE vorname LIKE 'Bryn'; -- Update Chip Count
SELECT vorname, chipzahl FROM ChipLeader WHERE vorname LIKE 'Bryn'; -- Check new Chip Count
