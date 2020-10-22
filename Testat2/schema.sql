/*
 * Tabellen erzeugen
 */


CREATE TABLE spieler (
    id INTEGER PRIMARY KEY,
    vorname VARCHAR(50) NOT NULL,
    nachname VARCHAR(50) NOT NULL,
    chipzahl INTEGER NOT NULL,
    aktiv BOOLEAN
);


CREATE TABLE floorman (
    id INTEGER PRIMARY KEY,
    vorname VARCHAR(50) NOT NULL,
    nachname VARCHAR(50) NOT NULL,
    erfahrung INTEGER NOT NULL
);

CREATE TABLE tournament (
    id INTEGER PRIMARY KEY,
    maxspieler INTEGER NOT NULL,
    preisgeld INTEGER NOT NULL,
    datum DATE NOT NULL,
    ort VARCHAR(80) NOT NULL,
    floorman INTEGER NOT NULL REFERENCES floorman(id)
);

CREATE TABLE profi (
    spielerid INTEGER NOT NULL REFERENCES spieler(id),
    rank INTEGER NOT NULL,
    tournament INTEGER NOT NULL REFERENCES tournament(id)
);

CREATE TABLE qualifying (
    id INTEGER PRIMARY KEY,
    startdatum DATE NOT NULL,
    endedatum DATE NOT NULL
);

CREATE TABLE beginner (
    spielerid INTEGER NOT NULL REFERENCES spieler(id),
    zugelassen BOOLEAN NOT NULL,
);

CREATE TABLE qualifyingspieler (
    id INTEGER NOT NULL REFERENCES qualifying(id),
    spielerid INTEGER NOT NULL REFERENCES spieler(id)
);
