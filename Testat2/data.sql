/*
 * Daten einfüllen
 */

INSERT INTO spieler (id, vorname, nachname, chipzahl, aktiv) VALUES
    -- Profis
    (1, 'Daniel', 'Negreanu', 100000, true),
    (2, 'Phil', 'Ivey', 100000, true),
    (3, 'Bryn', 'Kenney', 100000, true),
    (4, 'Fedor', 'Holz', 100000, true),
    (5, 'Antonio', 'Esfandiari', 100000, true),
    (6, 'Vanessa', 'Selbst', 100000, true),
    -- Beginner
    (7, 'Ole', 'Schemion', 100000, true),
    (8, 'Ioana', 'Dickerson', 100000, true),
    (9, 'Alisha', 'Tillman', 100000, true),
    (10, 'Maise', 'Burke', 100000, true),
    (11, 'Peter', 'Gray', 100000, true),
    (12, 'Issac', 'Myers', 100000, true),
    (13, 'Jaidon', 'Mill', 100000, true),
    (14, 'Hussain', 'Gale', 100000, true),
    (15, 'Jimmy', 'Blevins', 100000, true);

INSERT INTO floorman (id, vorname, nachname, erfahrung) VALUES
    (1, 'James', 'Hartigan', 9),
    (1, 'Joe', 'Stapleton', 9),
    (1, 'Kara', 'Scott', 9),
    (1, 'Lon', 'McEachern', 9),
    (1, 'Maria', 'Ho', 9);

INSERT INTO tournament (id, maxspieler, preisgeld, datum, ort, floorman) VALUES
    ()

INSERT INTO profi (spielerid, rank, tournament) VALUES
    (1, 10, 1)
