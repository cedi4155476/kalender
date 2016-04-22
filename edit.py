# -*- coding: utf-8 -*-

"""
Module implementing Edit.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_edit import Ui_Edit


class Edit(QDialog, Ui_Edit):
    """
    Class documentation goes here.
    """
    def __init__(self, c, conn, day, date, parent=None):
        """
        Set all LineEdits if they already exist
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.c = c
        self.conn = conn
        self.date = unicode(date)

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle(day + " " + date)

        self.c.execute('''SELECT * FROM Charakter''')
        characters = self.c.fetchall()
        if characters:
            self.characterlayout = self.characterW.layout()
            self.charactergroup = QButtonGroup(self.characterlayout)
            self.charactergroup.setExclusive(False)
            for character in characters:
                fullname = character['vorname'] + " " + character['nachname']
                checkbox = QCheckBox(fullname)
                checkbox.setWhatsThis(self.getValidString(character['id']))
                self.charactergroup.addButton(checkbox)
                self.characterlayout.addWidget(checkbox)

        self.c.execute('''SELECT * FROM Geschichte''')
        geschichten = self.c.fetchall()
        if geschichten:
            self.geschichtelayout = self.geschichteW.layout()
            self.geschichtegroup = QButtonGroup(self.geschichtelayout)
            self.geschichtegroup.setExclusive(False)
            for geschichte in geschichten:
                titel = geschichte['titel']
                checkbox = QCheckBox(titel)
                checkbox.setWhatsThis(self.getValidString(geschichte['id']))
                self.geschichtegroup.addButton(checkbox)
                self.geschichtelayout.addWidget(checkbox)

        self.c.execute('''SELECT * FROM Notiz WHERE tag=?''', (self.date,))
        notizen = self.c.fetchall()
        for notiz in notizen:
            if notiz['notiz'] != 'Geburt':
                self.titelCB.addItem(notiz['titel'], QVariant(notiz))

    def getValidString(self, value):
        if value:
            return QString(unicode(value))
        else:
            return QString()

    def check_characters(self):
        if hasattr(self, 'charactergroup'):
            notiz_id = self.id
            self.c.execute('''SELECT charakter_id FROM Notiz_Charakter WHERE notiz_id=?''', (notiz_id,))
            character_ids = self.c.fetchall()
            for character in self.charactergroup.buttons():
                character.setChecked(False)
                for character_id in character_ids:
                    if int(character.whatsThis()) == int(character_id['charakter_id']):
                        character.setChecked(True)

    def check_geschichten(self):
        if hasattr(self, 'geschichtegroup'):
            notiz_id = self.id
            self.c.execute('''SELECT geschichte_id FROM Geschichte_Notiz WHERE notiz_id=?''', (notiz_id,))
            geschichte_ids = self.c.fetchall()
            for geschichte in self.geschichtegroup.buttons():
                geschichte.setChecked(False)
                for geschichte_id in geschichte_ids:
                    if int(geschichte.whatsThis()) == int(geschichte_id['geschichte_id']):
                        geschichte.setChecked(True)

    @pyqtSignature("int")
    def on_titelCB_currentIndexChanged(self, index):
        if index > 0:
            objects = self.titelCB.itemData(index).toPyObject()
            self.notizTE.setPlainText(objects[QString('notiz')])
            self.inhaltTE.setPlainText(objects[QString('inhalt')])
            self.titelLE.setText(objects[QString('titel')])
            self.id = objects[QString('id')]
            self.check_characters()
            self.check_geschichten()
        else:
            self.notizTE.clear()
            self.inhaltTE.clear()
            self.titelLE.clear()
            self.id = None
            if hasattr(self, 'charactergroup'):
                for button in self.charactergroup.buttons():
                    button.setChecked(False)
            if hasattr(self, 'geschichtegroup'):
                for button in self.geschichtegroup.buttons():
                    button.setChecked(False)

    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        titel = unicode(self.titelLE.text())
        welt = unicode(self.weltCB.itemText(self.weltCB.currentIndex()))
        notiz = unicode(self.notizTE.toPlainText())
        inhalt = unicode(self.inhaltTE.toPlainText())
        date = self.date
        geschichten = []
        characters = []

        if hasattr(self, 'charactergroup'):
            characterbuttons = self.charactergroup.buttons()
            for button in characterbuttons:
                if button.isChecked():
                    characters.append(button.whatsThis())

        if hasattr(self, 'geschichtegroup'):
            geschichtebuttons = self.geschichtegroup.buttons()
            for button in geschichtebuttons:
                if button.isChecked():
                    geschichten.append(button.whatsThis())

        if self.titelCB.currentIndex() == 0:
            addnotiz = (None, titel, date, welt, notiz, inhalt)
            self.c.execute('''INSERT INTO Notiz VALUES (?,?,?,?,?,?)''', addnotiz)
            notiz_id = self.c.lastrowid

            for character in characters:
                addncbind = (notiz_id, int(character))
                self.c.execute('''INSERT INTO Notiz_Charakter VALUES (?,?)''', addncbind)

            for geschichte in geschichten:
                addgnbind = (int(geschichte), notiz_id)
                self.c.execute('''INSERT INTO Geschichte_Notiz VALUES (?,?)''', addgnbind)
        else:
            notiz_id = self.id
            changenotiz = (titel, welt, notiz, inhalt, self.id)
            self.c.execute('''UPDATE Notiz SET titel=?, welt=?, notiz=?, inhalt=? WHERE id=?''', changenotiz)

            self.c.execute('''DELETE FROM Notiz_Charakter WHERE notiz_id=?''', (notiz_id,))
            for character in characters:
                changencbind = (notiz_id, int(character))
                self.c.execute('''INSERT INTO Notiz_Charakter VALUES (?,?)''', changencbind)

            self.c.execute('''DELETE FROM Geschichte_Notiz WHERE notiz_id=?''', (notiz_id,))
            for geschichte in geschichten:
                changegnbind = (int(geschichte), notiz_id)
                self.c.execute('''INSERT INTO Geschichte_Notiz VALUES (?,?)''', changegnbind)
            self.titelCB.removeItem(self.titelCB.currentIndex())
        self.c.execute('''SELECT * FROM Notiz WHERE id=?''', (notiz_id,))
        notiz = self.c.fetchone()
        self.titelCB.addItem(notiz['titel'], QVariant(notiz))
        self.titelCB.setCurrentIndex(self.titelCB.count() - 1)

    def on_deleteBT_clicked(self):
        if self.id:
            notiz_id = self.id
            self.c.execute('''DELETE FROM Notiz WHERE id=?''', (notiz_id,))
            self.c.execute('''DELETE FROM Notiz_Charakter WHERE notiz_id=?''', (notiz_id,))
            self.c.execute('''DELETE FROM Geschichte_Notiz WHERE notiz_id=?''', (notiz_id,))
            self.titelCB.removeItem(self.titelCB.currentIndex())
            self.titelCB.setCurrentIndex(0)
