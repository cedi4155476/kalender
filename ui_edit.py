# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edit.ui'
#
# Created: Tue Mar 15 11:46:10 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Edit(object):
    def setupUi(self, Edit):
        Edit.setObjectName(_fromUtf8("Edit"))
        Edit.setWindowModality(QtCore.Qt.ApplicationModal)
        Edit.resize(299, 488)
        self.verticalLayout = QtGui.QVBoxLayout(Edit)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.weltCB = QtGui.QComboBox(Edit)
        self.weltCB.setObjectName(_fromUtf8("weltCB"))
        self.weltCB.addItem(_fromUtf8(""))
        self.weltCB.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.weltCB)
        self.titelCB = QtGui.QComboBox(Edit)
        self.titelCB.setObjectName(_fromUtf8("titelCB"))
        self.titelCB.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.titelCB)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.geschichtePB = QtGui.QPushButton(Edit)
        self.geschichtePB.setObjectName(_fromUtf8("geschichtePB"))
        self.horizontalLayout_2.addWidget(self.geschichtePB)
        self.charakterePB = QtGui.QPushButton(Edit)
        self.charakterePB.setObjectName(_fromUtf8("charakterePB"))
        self.horizontalLayout_2.addWidget(self.charakterePB)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Edit)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.titelLE = QtGui.QLineEdit(Edit)
        self.titelLE.setObjectName(_fromUtf8("titelLE"))
        self.horizontalLayout.addWidget(self.titelLE)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtGui.QLabel(Edit)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.notizTE = QtGui.QTextEdit(Edit)
        self.notizTE.setMaximumSize(QtCore.QSize(16777215, 100))
        self.notizTE.setObjectName(_fromUtf8("notizTE"))
        self.verticalLayout.addWidget(self.notizTE)
        self.label_2 = QtGui.QLabel(Edit)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.inhaltTE = QtGui.QTextEdit(Edit)
        self.inhaltTE.setObjectName(_fromUtf8("inhaltTE"))
        self.verticalLayout.addWidget(self.inhaltTE)
        self.buttonBox = QtGui.QDialogButtonBox(Edit)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Edit)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Edit.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Edit.reject)
        QtCore.QMetaObject.connectSlotsByName(Edit)

    def retranslateUi(self, Edit):
        Edit.setWindowTitle(_translate("Edit", "Bearbeiten", None))
        self.weltCB.setItemText(0, _translate("Edit", "Menschenwelt", None))
        self.weltCB.setItemText(1, _translate("Edit", "Dämonenwelt", None))
        self.titelCB.setItemText(0, _translate("Edit", "Neu erstellen", None))
        self.geschichtePB.setText(_translate("Edit", "Geschichte", None))
        self.charakterePB.setText(_translate("Edit", "Charaktere", None))
        self.label.setText(_translate("Edit", "Titel:", None))
        self.label_3.setText(_translate("Edit", "Notizen:", None))
        self.label_2.setText(_translate("Edit", "Inhalt:", None))

