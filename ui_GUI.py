# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_GUI.ui'
#
# Created: Tue Mar 22 12:55:06 2016
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(773, 488)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.frame)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.storycreatePB = QtGui.QPushButton(self.tab_2)
        self.storycreatePB.setObjectName(_fromUtf8("storycreatePB"))
        self.horizontalLayout_4.addWidget(self.storycreatePB)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.storyTW = QtGui.QTableWidget(self.tab_2)
        self.storyTW.setFrameShape(QtGui.QFrame.NoFrame)
        self.storyTW.setFrameShadow(QtGui.QFrame.Plain)
        self.storyTW.setLineWidth(0)
        self.storyTW.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.storyTW.setTabKeyNavigation(False)
        self.storyTW.setProperty("showDropIndicator", False)
        self.storyTW.setDragDropOverwriteMode(False)
        self.storyTW.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.storyTW.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.storyTW.setShowGrid(False)
        self.storyTW.setGridStyle(QtCore.Qt.NoPen)
        self.storyTW.setWordWrap(False)
        self.storyTW.setCornerButtonEnabled(False)
        self.storyTW.setObjectName(_fromUtf8("storyTW"))
        self.storyTW.setColumnCount(5)
        self.storyTW.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.storyTW.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.storyTW.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.storyTW.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.storyTW.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.storyTW.setHorizontalHeaderItem(4, item)
        self.storyTW.horizontalHeader().setVisible(False)
        self.storyTW.horizontalHeader().setHighlightSections(False)
        self.storyTW.verticalHeader().setVisible(False)
        self.storyTW.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.storyTW)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.charactercreatePB = QtGui.QPushButton(self.tab)
        self.charactercreatePB.setObjectName(_fromUtf8("charactercreatePB"))
        self.horizontalLayout_5.addWidget(self.charactercreatePB)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.characterTW = QtGui.QTableWidget(self.tab)
        self.characterTW.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.characterTW.setProperty("showDropIndicator", False)
        self.characterTW.setDragDropOverwriteMode(False)
        self.characterTW.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.characterTW.setObjectName(_fromUtf8("characterTW"))
        self.characterTW.setColumnCount(6)
        self.characterTW.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.characterTW.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.characterTW.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.characterTW.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.characterTW.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.characterTW.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.characterTW.setHorizontalHeaderItem(5, item)
        self.characterTW.horizontalHeader().setVisible(False)
        self.characterTW.horizontalHeader().setHighlightSections(False)
        self.characterTW.verticalHeader().setVisible(False)
        self.characterTW.verticalHeader().setHighlightSections(False)
        self.verticalLayout_4.addWidget(self.characterTW)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.month = QtGui.QWidget()
        self.month.setObjectName(_fromUtf8("month"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.month)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.previousB = QtGui.QPushButton(self.month)
        self.previousB.setObjectName(_fromUtf8("previousB"))
        self.horizontalLayout_2.addWidget(self.previousB)
        self.monthLabel = QtGui.QLabel(self.month)
        self.monthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.monthLabel.setObjectName(_fromUtf8("monthLabel"))
        self.horizontalLayout_2.addWidget(self.monthLabel)
        self.nextB = QtGui.QPushButton(self.month)
        self.nextB.setObjectName(_fromUtf8("nextB"))
        self.horizontalLayout_2.addWidget(self.nextB)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.monthTW = MyTableWidget(self.month)
        self.monthTW.setFrameShape(QtGui.QFrame.NoFrame)
        self.monthTW.setFrameShadow(QtGui.QFrame.Plain)
        self.monthTW.setLineWidth(0)
        self.monthTW.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.monthTW.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.monthTW.setAutoScroll(False)
        self.monthTW.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.monthTW.setProperty("showDropIndicator", False)
        self.monthTW.setDragDropOverwriteMode(False)
        self.monthTW.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.monthTW.setShowGrid(False)
        self.monthTW.setGridStyle(QtCore.Qt.NoPen)
        self.monthTW.setCornerButtonEnabled(False)
        self.monthTW.setRowCount(7)
        self.monthTW.setColumnCount(7)
        self.monthTW.setObjectName(_fromUtf8("monthTW"))
        item = QtGui.QTableWidgetItem()
        self.monthTW.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        self.monthTW.setItem(0, 6, item)
        self.monthTW.horizontalHeader().setVisible(False)
        self.monthTW.horizontalHeader().setCascadingSectionResizes(False)
        self.monthTW.horizontalHeader().setHighlightSections(False)
        self.monthTW.horizontalHeader().setSortIndicatorShown(False)
        self.monthTW.horizontalHeader().setStretchLastSection(False)
        self.monthTW.verticalHeader().setVisible(False)
        self.monthTW.verticalHeader().setHighlightSections(False)
        self.verticalLayout_2.addWidget(self.monthTW)
        self.tabWidget.addTab(self.month, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 773, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuData = QtGui.QMenu(self.menuBar)
        self.menuData.setObjectName(_fromUtf8("menuData"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionSchliessen = QtGui.QAction(MainWindow)
        self.actionSchliessen.setObjectName(_fromUtf8("actionSchliessen"))
        self.actionAddStory = QtGui.QAction(MainWindow)
        self.actionAddStory.setObjectName(_fromUtf8("actionAddStory"))
        self.menuData.addAction(self.actionSchliessen)
        self.menuEdit.addAction(self.actionAddStory)
        self.menuBar.addAction(self.menuData.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Kalender", None))
        self.label.setText(_translate("MainWindow", "Filter", None))
        self.label_2.setText(_translate("MainWindow", "Suche", None))
        self.storycreatePB.setText(_translate("MainWindow", "Neue Geschichte", None))
        item = self.storyTW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Titel", None))
        item = self.storyTW.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Datei", None))
        item = self.storyTW.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Pfad", None))
        item = self.storyTW.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Kurzinfo", None))
        item = self.storyTW.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Löschen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Geschichten", None))
        self.charactercreatePB.setText(_translate("MainWindow", "Neuer Charakter", None))
        item = self.characterTW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Vorname", None))
        item = self.characterTW.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nachname", None))
        item = self.characterTW.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Geburtsdatum", None))
        item = self.characterTW.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Info", None))
        item = self.characterTW.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Bearbeiten", None))
        item = self.characterTW.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Löschen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Charaktere", None))
        self.previousB.setText(_translate("MainWindow", "Letzter Monat", None))
        self.monthLabel.setText(_translate("MainWindow", "Monat", None))
        self.nextB.setText(_translate("MainWindow", "Nächster Monat", None))
        item = self.monthTW.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.monthTW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Montag", None))
        item = self.monthTW.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Neue Spalte", None))
        item = self.monthTW.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Dienstag", None))
        item = self.monthTW.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mittwoch", None))
        item = self.monthTW.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Donnerstag", None))
        item = self.monthTW.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Freitag", None))
        item = self.monthTW.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sonntag", None))
        __sortingEnabled = self.monthTW.isSortingEnabled()
        self.monthTW.setSortingEnabled(False)
        item = self.monthTW.item(0, 0)
        item.setText(_translate("MainWindow", "Montag", None))
        item = self.monthTW.item(0, 1)
        item.setText(_translate("MainWindow", "Dienstag", None))
        item = self.monthTW.item(0, 2)
        item.setText(_translate("MainWindow", "Mittwoch", None))
        item = self.monthTW.item(0, 3)
        item.setText(_translate("MainWindow", "Donnerstag", None))
        item = self.monthTW.item(0, 4)
        item.setText(_translate("MainWindow", "Freitag", None))
        item = self.monthTW.item(0, 5)
        item.setText(_translate("MainWindow", "Samstag", None))
        item = self.monthTW.item(0, 6)
        item.setText(_translate("MainWindow", "Sonntag", None))
        self.monthTW.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.month), _translate("MainWindow", "Monatsansicht", None))
        self.menuData.setTitle(_translate("MainWindow", "Datei", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Bearbeiten", None))
        self.actionSchliessen.setText(_translate("MainWindow", "Schliessen", None))
        self.actionSchliessen.setWhatsThis(_translate("MainWindow", "close", None))
        self.actionAddStory.setText(_translate("MainWindow", "Geschichte hinzufügen", None))
        self.actionAddStory.setWhatsThis(_translate("MainWindow", "addstory", None))

from myTableWidget import MyTableWidget
