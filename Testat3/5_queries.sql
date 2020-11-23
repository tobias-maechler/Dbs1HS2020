-- Autoren: Kevin Löffler & Tobias Mächler

-- 1.1 Distinct:
\prompt 'Execute Distinct Query (\\q or Ctrl-C to abort)?' promptvar
:promptvar

SELECT count(DISTINCT ort) AS "Anzahl Veranstaltungsorte" FROM tournament;

-- 1.2 Join:
\prompt 'Execute Join Query (\\q or Ctrl-C to abort)?' promptvar
:promptvar

SELECT spieler.vorname AS "Vorname", spieler.nachname AS "Nachname", tournament.id AS "Tournament Nr.", tournament.ort AS "Austragungsort" FROM spieler JOIN profi ON profi.spielerid = spieler.id JOIN tournament ON profi.tournament = tournament.id ORDER BY spieler.nachname LIMIT 20;

-- 1.3 Uncorrelated Subquery
\prompt 'Execute Uncorrelated Subquery (\\q or Ctrl-C to abort)?' promptvar
:promptvar

SELECT vorname, nachname, gewinn FROM spieler WHERE gewinn > (SELECT AVG(gewinn) FROM spieler WHERE aktiv = true) ORDER BY gewinn DESC LIMIT 20;

-- 1.4 Statement:
\prompt 'Execute Query with Exists Statement (\\q or Ctrl-C to abort)?' promptvar
:promptvar

SELECT vorname, nachname FROM spieler s WHERE EXISTS (SELECT * FROM profi WHERE spielerid = s.id) ORDER BY nachname LIMIT 20;


-- 2.1 Common Table Expressions/WITH-Statements:
-- Uncorrelated Subquery
\prompt 'Execute uncorrelated Subquery (\\q or Ctrl-C to abort)?' promptvar
:promptvar

SELECT vorname, nachname, gewinn FROM spieler JOIN beginner ON spieler.id = beginner.spielerid WHERE gewinn > (SELECT AVG(gewinn) FROM spieler) ORDER BY gewinn DESC LIMIT 20;

-- Converted to Common Table Expression:
\prompt 'Execute Common Table Expression Query (\\q or Ctrl-C to abort)?' promptvar
:promptvar
WITH
aboveAverage AS
(SELECT id, vorname, nachname, gewinn FROM spieler WHERE gewinn > (SELECT AVG(gewinn) FROM spieler)),
allBeginner AS
(SELECT spieler.id FROM spieler JOIN beginner ON spieler.id = beginner.spielerid)
SELECT aboveAverage.vorname, aboveAverage.nachname, aboveAverage.gewinn FROM aboveAverage JOIN allBeginner ON aboveAverage.id = allBeginner.id ORDER BY gewinn DESC LIMIT 20;


-- 2.2 GROUP-BY und Window-Funktion:

-- GROUP-BY:
\prompt 'Execute GROUP-BY Query (\\q or Ctrl-C to abort)?' promptvar
:promptvar

SELECT ort AS "Veranstaltungs Ort", COUNT(*) AS "Anzahl Turniere" FROM tournament GROUP BY ort ORDER BY ort LIMIT 20;

-- Window Function:
\prompt 'Execute Window Function Query (\\q or Ctrl-C to abort)?' promptvar
:promptvar

SELECT vorname AS "Vorname", nachname AS "Nachname", gewinn AS "Gewinn", gewinn - lead(gewinn,1,gewinn) OVER (ORDER BY gewinn) AS "Vergleich" FROM spieler ORDER BY 3 DESC LIMIT 20;


-- 3.1 View:
\prompt 'Create View (\\q or Ctrl-C to abort)?' promptvar
:promptvar

CREATE VIEW Teilnehmer AS SELECT spieler.vorname AS "Vorname", spieler.nachname AS "Nachname", tournament.id AS "Tournament Nr.", tournament.ort AS "Austragungsort" FROM spieler JOIN profi ON profi.spielerid = spieler.id JOIN tournament ON profi.tournament = tournament.id;
SELECT * FROM Teilnehmer LIMIT 20;

--3.2 Update View:
\prompt 'Create another View (\\q or Ctrl-C to abort)?' promptvar
:promptvar

CREATE VIEW ChipLeader AS SELECT vorname, nachname, chipzahl FROM spieler ORDER BY chipzahl DESC;

\prompt 'Check the chipcount before update the view (\\q or Ctrl-C to abort)?' promptvar
:promptvar

SELECT vorname, chipzahl FROM ChipLeader WHERE vorname LIKE 'Bryn';

\prompt 'Updating the view and set chipcount to 10 (\\q or Ctrl-C to abort)?' promptvar
:promptvar

UPDATE ChipLeader SET chipzahl = 10 WHERE vorname LIKE 'Bryn';

\prompt 'Check updated chipcount again (\\q or Ctrl-C to abort)?' promptvar
:promptvar

SELECT vorname, chipzahl FROM ChipLeader WHERE vorname LIKE 'Bryn';
