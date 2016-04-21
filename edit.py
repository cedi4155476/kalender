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
        self.characterlayout = self.characterW.layout()
        self.charactergroup = QButtonGroup(self.characterlayout)
        self.charactergroup.setExclusive(False)
        for character in characters:
            fullname = character['vorname'] + " " + character['nachname']
            checkbox = QCheckBox(fullname)
            checkbox.setWhatsThis(self.getValidString(character['id']))
            self.charactergroup.addButton(checkbox)
            self.characterlayout.addWidget(checkbox)

        self.c.execute('''SELECT * FROM Notiz WHERE tag=?''', (self.date,))
        notizen = self.c.fetchall()
        for notiz in notizen:
            self.titelCB.addItem(notiz['titel'], QVariant(notiz))

    def getValidString(self, value):
        if value:
            return QString(unicode(value))
        else:
            return QString()

    @pyqtSignature("int")
    def on_titelCB_currentIndexChanged(self, index):
        if index > 0:
            objects = self.titelCB.itemData(index).toPyObject()
            self.notizTE.setPlainText(objects[QString('notiz')])
            self.inhaltTE.setPlainText(objects[QString('inhalt')])
            self.titelLE.setText(objects[QString('titel')])
            self.id = objects[QString('id')]
        else:
            self.notizTE.clear()
            self.inhaltTE.clear()
            self.titelLE.clear()
            self.id = None

    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        titel = unicode(self.titelLE.text())
        welt = unicode(self.weltCB.itemText(self.weltCB.currentIndex()))
        buttons = self.charactergroup.buttons()
        notiz = unicode(self.notizTE.toPlainText())
        inhalt = unicode(self.inhaltTE.toPlainText())
        date = self.date
        characters = []
        for button in buttons:
            if button.isChecked():
                characters.append(button.whatsThis())
        if self.titelCB.currentIndex() == 0:
            addnotiz = (None, titel, date, welt, notiz, inhalt)
            self.c.execute('''INSERT INTO Notiz VALUES (?,?,?,?,?,?)''', addnotiz)
            notiz_id = self.c.lastrowid

            for character in characters:
                addncbind = (notiz_id, int(character))
                self.c.execute('''INSERT INTO Notiz_Charakter VALUES (?,?)''', addncbind)
        else:
            changenotiz = (titel, welt, notiz, inhalt, self.id)
            self.c.execute('''UPDATE Notiz SET titel=?, welt=?, notiz=?, inhalt=? WHERE id=?''', changenotiz)

            self.c.execute('''DELETE FROM Notiz_Charakter WHERE notiz_id=?''', (self.id,))

            for character in characters:
                changencbind = (self.id, int(character))
                self.c.execute('''INSERT INTO Notiz_Charakter VALUES (?,?)''', addncbind)

        self.accept()
