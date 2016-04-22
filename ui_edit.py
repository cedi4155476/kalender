# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edit.ui'
#
# Created: Fri Apr 22 11:31:45 2016
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
        Edit.resize(299, 516)
        self.verticalLayout = QtGui.QVBoxLayout(Edit)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.weltCB = QtGui.QComboBox(Edit)
        self.weltCB.setObjectName(_fromUtf8("weltCB"))
        self.weltCB.addItem(_fromUtf8(""))
        self.weltCB.addItem(_fromUtf8(""))
        self.weltCB.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.weltCB)
        self.titelCB = QtGui.QComboBox(Edit)
        self.titelCB.setObjectName(_fromUtf8("titelCB"))
        self.titelCB.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.titelCB)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Edit)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.titelLE = QtGui.QLineEdit(Edit)
        self.titelLE.setObjectName(_fromUtf8("titelLE"))
        self.horizontalLayout.addWidget(self.titelLE)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_4 = QtGui.QLabel(Edit)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.storySA = QtGui.QScrollArea(Edit)
        self.storySA.setWidgetResizable(True)
        self.storySA.setObjectName(_fromUtf8("storySA"))
        self.geschichteW = QtGui.QWidget()
        self.geschichteW.setGeometry(QtCore.QRect(0, 0, 285, 70))
        self.geschichteW.setObjectName(_fromUtf8("geschichteW"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.geschichteW)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.storySA.setWidget(self.geschichteW)
        self.verticalLayout.addWidget(self.storySA)
        self.label_5 = QtGui.QLabel(Edit)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.characterSA = QtGui.QScrollArea(Edit)
        self.characterSA.setWidgetResizable(True)
        self.characterSA.setObjectName(_fromUtf8("characterSA"))
        self.characterW = QtGui.QWidget()
        self.characterW.setGeometry(QtCore.QRect(0, 0, 285, 70))
        self.characterW.setObjectName(_fromUtf8("characterW"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.characterW)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.characterSA.setWidget(self.characterW)
        self.verticalLayout.addWidget(self.characterSA)
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
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.deleteBT = QtGui.QPushButton(Edit)
        self.deleteBT.setObjectName(_fromUtf8("deleteBT"))
        self.horizontalLayout_2.addWidget(self.deleteBT)
        self.buttonBox = QtGui.QDialogButtonBox(Edit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Edit)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Edit.reject)
        QtCore.QMetaObject.connectSlotsByName(Edit)

    def retranslateUi(self, Edit):
        Edit.setWindowTitle(_translate("Edit", "Bearbeiten", None))
        self.weltCB.setItemText(0, _translate("Edit", "0", None))
        self.weltCB.setItemText(1, _translate("Edit", "Menschenwelt", None))
        self.weltCB.setItemText(2, _translate("Edit", "Dämonenwelt", None))
        self.titelCB.setItemText(0, _translate("Edit", "Neu erstellen", None))
        self.label.setText(_translate("Edit", "Titel:", None))
        self.label_4.setText(_translate("Edit", "Geschichten:", None))
        self.label_5.setText(_translate("Edit", "Charaktere:", None))
        self.label_3.setText(_translate("Edit", "Notizen:", None))
        self.label_2.setText(_translate("Edit", "Inhalt:", None))
        self.deleteBT.setText(_translate("Edit", "Löschen", None))

