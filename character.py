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
            addstory = (None, vorname, nachname, geburtstag, info)
            self.c.execute('''INSERT INTO Charakter VALUES (?,?,?,?,?) ''', addstory)
        else:
            changestory = (vorname, nachname, geburtstag, info, self.id)
            self.c.execute('''UPDATE Charakter SET vorname=?, nachname=?, geburstag=?, info=? WHERE id=?''', changestory)

        self.accept()
