# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_character.ui'
#
# Created: Tue Mar 22 12:48:54 2016
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

class Ui_Character(object):
    def setupUi(self, Character):
        Character.setObjectName(_fromUtf8("Character"))
        Character.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Character)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Character)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.vornameLE = QtGui.QLineEdit(Character)
        self.vornameLE.setObjectName(_fromUtf8("vornameLE"))
        self.horizontalLayout.addWidget(self.vornameLE)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(Character)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.nachnameLE = QtGui.QLineEdit(Character)
        self.nachnameLE.setObjectName(_fromUtf8("nachnameLE"))
        self.horizontalLayout_2.addWidget(self.nachnameLE)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(Character)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.geburtstagLE = QtGui.QLineEdit(Character)
        self.geburtstagLE.setObjectName(_fromUtf8("geburtstagLE"))
        self.horizontalLayout_3.addWidget(self.geburtstagLE)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_2 = QtGui.QLabel(Character)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.infoTE = QtGui.QTextEdit(Character)
        self.infoTE.setObjectName(_fromUtf8("infoTE"))
        self.verticalLayout.addWidget(self.infoTE)
        self.buttonBox = QtGui.QDialogButtonBox(Character)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Character)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Character.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Character.reject)
        QtCore.QMetaObject.connectSlotsByName(Character)

    def retranslateUi(self, Character):
        Character.setWindowTitle(_translate("Character", "Charakter hinzufügen", None))
        self.label.setText(_translate("Character", "Vorname:", None))
        self.label_3.setText(_translate("Character", "Nachname:", None))
        self.label_4.setText(_translate("Character", "Gebursttag:", None))
        self.label_2.setText(_translate("Character", "Info:", None))

