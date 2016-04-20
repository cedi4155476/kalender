BEGIN TRANSACTION;
CREATE TABLE Charakter (id INTEGER PRIMARY KEY, vorname TEXT, nachname TEXT, geburtstag TEXT, info TEXT);
CREATE TABLE Notiz (id INTEGER PRIMARY KEY, tag TEXT, welt TEXT, notiz TEXT, inhalt TEXT);
CREATE TABLE Geschichte (id INTEGER PRIMARY KEY, titel TEXT, kurzinfo TEXT, pfad TEXT);
CREATE TABLE Geschichte_Charakter (geschichte_id NUMERIC, charakter_id NUMERIC);
CREATE TABLE Geschichte_Notiz (geschichte_id NUMERIC, notiz_id NUMERIC);
CREATE TABLE Notiz_Charakter (notiz_id NUMERIC, charakter_id NUMERIC);
COMMIT;
