# -*- coding: utf-8 -*-

"""
Module implementing Edit.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_character import Ui_Character


class Character(QDialog, Ui_Character):
    """
    Class documentation goes here.
    """
    def __init__(self, data, c, conn, parent=None):
        """
        Set all LineEdits if they already exist
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.data = data
        self.c = c
        self.conn = conn

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        if data:
            self.id = data['id']
            self.vornameLE.setText(self.getValidString(data['vorname']))
            self.nachnameLE.setText(self.getValidString(data['nachname']))
            self.geburtstagLE.setText(self.getValidString(data['geburtstag']))
            self.infoTE.insertPlainText(self.getValidString(data['info']))

    def getValidString(self, value):
        if value:
            return QString(unicode(value))
        else:
            return QString()

    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        """
        send directory informations
        """
        vorname = unicode(self.vornameLE.text())
        nachname = unicode(self.nachnameLE.text())
        geburtstag = unicode(self.geburtstagLE.text())
        info = unicode(self.infoTE.toPlainText())

        if not self.data:
            addcharacter = (None, vorname, nachname, geburtstag, info)
            geburtstag_fullname = "Geburtstag von " + vorname + " " + nachname
            addnotiz = (None, geburtstag, 0, "Geburtstag", geburtstag_fullname)
            self.c.execute('''INSERT INTO Charakter VALUES (?,?,?,?,?) ''', addcharacter)
            self.c.execute('''INSERT INTO Notiz VALUES (?,?,?,?,?) ''', addnotiz)

            fullname = (vorname, nachname)
            self.c.execute('''SELECT id FROM Charakter WHERE vorname=? AND nachname=?''', fullname)
            character_id = self.c.fetchone()['id']
            self.c.execute('''SELECT id FROM Notiz WHERE inhalt=?''', (geburtstag_fullname,))
            notiz_id = self.c.fetchone()['id']
            addbind = (notiz_id, character_id)
            self.c.execute('''INSERT INTO Notiz_Charakter VALUES (?,?) ''', addbind)
        else:
            changecharacter = (vorname, nachname, geburtstag, info, self.id)
            self.c.execute('''UPDATE Charakter SET vorname=?, nachname=?, geburstag=?, info=? WHERE id=?''', changecharacter)

        self.accept()
