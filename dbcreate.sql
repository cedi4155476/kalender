BEGIN TRANSACTION;
CREATE TABLE Charakter (id INTEGER PRIMARY KEY, vorname TEXT, nachname TEXT, geburtstag TEXT, info TEXT);
CREATE TABLE Notiz (id INTEGER PRIMARY KEY, tag TEXT, charakter_id NUMERIC, geschichte NUMERIC, welt TEXT, notiz TEXT, inhalt TEXT);
CREATE TABLE Geschichte (id INTEGER PRIMARY KEY, titel TEXT, kurzinfo TEXT, pfad TEXT);
CREATE TABLE Geschichte_Charakter (geschichte_id NUMERIC, charakter_id NUMERIC);
COMMIT;
