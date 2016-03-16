# -*- coding: utf-8 -*-

"""
Module implementing Edit.
"""

from PyQt4.QtCore import pyqtSignature, QString, Qt
from PyQt4.QtGui import QDialog

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
        self.date = date

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle(day + " " + date)

    def getValidString(self, value):
        if value:
            return QString(unicode(value))
        else:
            return QString()

    # @pyqtSignature("QAbstractButton*")
    # def on_buttonBox_clicked(self, button):
    #     """
    #     Slot documentation goes here.
    #     """
    #     if button.text() == 'Save':
    #         self.accept()
    #     else:
    #         self.reject()
    #
    # @pyqtSignature("")
    # def on_editGenreButton_clicked(self):
    #     """
    #     Slot documentation goes here.
    #     """
    #     self.gdlg = Genre(self.c, self.conn, self.path)
    #     self.gdlg.exec_()
