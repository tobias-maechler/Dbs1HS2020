-- Autoren: Kevin Löffler & Tobias Mächler

INSERT INTO spieler (id, vorname, nachname, chipzahl, aktiv) VALUES
    -- Profis
    (1, 'Daniel', 'Negreanu', 2000000, 100000, true),
    (2, 'Phil', 'Ivey', 2000000, 100000, true),
    (3, 'Bryn', 'Kenney', 2000000, 100000, true),
    (4, 'Fedor', 'Holz', 2000000, 100000, true),
    (5, 'Antonio', 'Esfandiari', 2000000, 100000, true),
    (6, 'Vanessa', 'Selbst', 2000000, 100000, true),
    (7, 'Ole', 'Schemion', 2000000, 100000, true),
    -- Beginner
    (8, 'Ioana', 'Dickerson', 2000000, 100000, true),
    (9, 'Alisha', 'Tillman', 2000000, 100000, true),
    (10, 'Maise', 'Burke', 2000000, 100000, true),
    (11, 'Peter', 'Gray', 2000000, 100000, true),
    (12, 'Issac', 'Myers', 2000000, 100000, true),
    (13, 'Jaidon', 'Mill', 2000000, 100000, true),
    (14, 'Hussain', 'Gale', 2000000, 100000, true),
    (15, 'Jimmy', 'Blevins', 2000000, 100000, true);

INSERT INTO floorman (id, vorname, nachname, erfahrung) VALUES
    (1, 'James', 'Hartigan', 9),
    (2, 'Joe', 'Stapleton', 9),
    (3, 'Kara', 'Scott', 9),
    (4, 'Lon', 'McEachern', 9),
    (5, 'Maria', 'Ho', 9);

INSERT INTO tournament (id, maxspieler, preisgeld, datum, ort, floorman) VALUES
    (1, 8, 10000000, '2020-11-04', 'Las Vegas', 2);

INSERT INTO profi (spielerid, rank, tournament) VALUES
    (1, 10, 1),
    (2, 10, 1),
    (3, 7, 1),
    (4, 8, 1),
    (5, 9, 1),
    (6, 9, 1),
    (7, 8, 1);

INSERT INTO beginner (spielerid, zugelassen) VALUES
    (8, false),
    (9, false),
    (10, false),
    (11, false),
    (12, false),
    (13, false),
    (14, false),
    (15, false);

INSERT INTO qualifying (id, startdatum, endedatum) VALUES
    (1, '2020-10-08', '2020-10-10'),
    (2, '2020-10-9', '2020-10-20'),
    (3, '2020-10-16', '2020-11-02'),
    (4, '2020-11-05', '2020-11-20');

INSERT INTO qualifyingspieler (id, Spielerid) VALUES
    (1, 8),
    (1, 9),
    (1, 11),
    (1, 12),
    (2, 8),
    (2, 10),
    (2, 11),
    (2, 15),
    (3, 12),
    (3, 14),
    (3, 15),
    (4, 10),
    (4, 13),
    (4, 14),
    (4, 15);
