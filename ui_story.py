# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_story.ui'
#
# Created: Tue Mar 15 14:14:18 2016
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

class Ui_Story(object):
    def setupUi(self, Story):
        Story.setObjectName(_fromUtf8("Story"))
        Story.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Story)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Story)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.titelLE = QtGui.QLineEdit(Story)
        self.titelLE.setObjectName(_fromUtf8("titelLE"))
        self.horizontalLayout.addWidget(self.titelLE)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(Story)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.pathLE = QtGui.QLineEdit(Story)
        self.pathLE.setObjectName(_fromUtf8("pathLE"))
        self.horizontalLayout_2.addWidget(self.pathLE)
        self.searchPB = QtGui.QPushButton(Story)
        self.searchPB.setObjectName(_fromUtf8("searchPB"))
        self.horizontalLayout_2.addWidget(self.searchPB)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(Story)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.notizTE = QtGui.QTextEdit(Story)
        self.notizTE.setObjectName(_fromUtf8("notizTE"))
        self.verticalLayout.addWidget(self.notizTE)
        self.buttonBox = QtGui.QDialogButtonBox(Story)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Story)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Story.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Story.reject)
        QtCore.QMetaObject.connectSlotsByName(Story)

    def retranslateUi(self, Story):
        Story.setWindowTitle(_translate("Story", "Geschichte hinzufügen", None))
        self.label.setText(_translate("Story", "Titel:", None))
        self.label_3.setText(_translate("Story", "Pfad:", None))
        self.searchPB.setText(_translate("Story", "Durchsuchen...", None))
        self.label_2.setText(_translate("Story", "Kurznotiz:", None))

