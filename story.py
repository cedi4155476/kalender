# -*- coding: utf-8 -*-

"""
Module implementing Edit.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from os.path import expanduser

from ui_story import Ui_Story


class Story(QDialog, Ui_Story):
    """
    Class documentation goes here.
    """
    def __init__(self, c, conn, parent=None):
        """
        Set all LineEdits if they already exist
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.c = c
        self.conn = conn

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

    def getValidString(self, value):
        if value:
            return QString(unicode(value))
        else:
            return QString()

    @pyqtSignature("")
    def on_searchPB_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.pathLE.text():
            start = self.pathLE.text()
        else:
            start = expanduser("~")
        self.pathLE.setText(QFileDialog.getOpenFileName(self, "Choose file", start))

    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        """
        send directory informations
        """
        path = unicode(self.pathLE.text())
        title = unicode(self.titelLE.text())
        info = unicode(self.notizTE.toPlainText())

        addstory = (None, title, info, path)
        self.c.execute('''INSERT INTO Geschichte VALUES (?,?,?,?) ''', addstory)

        self.accept()
