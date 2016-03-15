# -*- coding: utf-8 -*-
"""
Module implementing MainWindow.
"""
import sqlite3
import os.path
import math
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui_GUI import Ui_MainWindow
from edit import Edit
from story import Story

mDAYS = ["Montag",
         "Dienstag",
         "Mittwoch",
         "Donnerstag",
         "Freitag",
         "Samstag",
         "Sonntag"]


mMONTHS = [["None", 0, 0],
           ["Januar", 1, 31],
           ["Februar", 2, 29],
           ["Maerz", 3, 31],
           ["April", 4, 30],
           ["May", 5, 31],
           ["Juni", 6, 30],
           ["July", 7, 31],
           ["August", 8, 31],
           ["September", 9, 30],
           ["Oktober", 10, 31],
           ["November", 11, 30],
           ["Dezember", 12, 31]]


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Das Hauptfenster wird erstellt und alle funktionen eingefügt.
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.db_connect()
        self.setupUi(self)
        self.installEventFilter()
        self.make_connections()
        self.initialisedmonth = False
        self.initialisedstories = False

    def db_connect(self):
        """
        connect to the db and if it did not exist make the db and it's tables
        """
        self.conn = sqlite3.connect('kalender.db')
        self.conn.row_factory = self.dict_factory
        self.c = self.conn.cursor()
        try:
            self.c.execute('SELECT tag FROM tag')
        except sqlite3.OperationalError:
            for line in open('dbcreate.sql'):
                try:
                    self.c.execute(line)
                except sqlite3.OperationalError:
                    break

    def installEventFilter(self):
        """
        install the Event Filters
        """
        pass

    def make_connections(self):
        """
        create the connects
        """
        pass

    def dict_factory(self, cursor, row):
        """
        make it easier to read from db
        """
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def getValidQTWI(self, value):
        """
        Make a valid qtablewidgetitem so it doesn't crash if it's empty
        """
        if value:
            return QTableWidgetItem(value)
        else:
            return QTableWidgetItem()

    @pyqtSignature("QAction*")
    def on_menuBar_triggered(self, action):
        """
        menu bar actions
        """
        if action.whatsThis() == "close":
            QApplication.quit()
        elif action.whatsThis() == "addstory":
            story = Story(self.c, self.conn, self)
            ret = story.exec_()
            if ret == QDialog.Accepted:
                self.conn.commit()
            else:
                self.conn.rollback()

    def on_tabWidget_currentChanged(self, tab):
        if tab == 0:
            if not self.initialisedstories:
                self.initialise_stories()
            self.create_stories()

        elif tab == 1:
            if not self.initialisedmonth:
                self.initialise_month()
            self.create_month()

    def initialise_stories(self):
        self.c.execute('''SELECT titel, kurzinfo, pfad FROM Geschichte''')
        self.storydatas = self.c.fetchall()
        self.initialisedstories = True

    def create_stories(self):
        i = 0
        self.storyTW.setRowCount(len(self.storydatas))
        for story in self.storydatas:
            editwidget = QWidget()
            editlayout = QBoxLayout(2, editwidget)
            editwidget.setLayout(editlayout)
            editbutton = QPushButton("bearbeiten")
            editlayout.addWidget(editbutton)

            deletewidget = QWidget()
            deletelayout = QBoxLayout(2, deletewidget)
            deletewidget.setLayout(deletelayout)
            deletebutton = QPushButton("bearbeiten")
            deletelayout.addWidget(deletebutton)
            self.storyTW.setItem(i, 0, self.getValidQTWI(unicode(story['titel'])))
            self.storyTW.setItem(i, 1, self.getValidQTWI(unicode(story['kurzinfo'])))
            self.storyTW.setItem(i, 2, self.getValidQTWI("Datei"))
            self.storyTW.setCellWidget(i, 3, editwidget)
            self.storyTW.setCellWidget(i, 4, deletewidget)
            i += 1

    def initialise_month(self):
        self.item = None
        self.d = 4
        self.month = mMONTHS[9]
        self.year = 580
        self.initialisedmonth = True

    def add_header_month(self):
        for i in range(len(mDAYS)):
            self.monthTW.setItem(0, i, self.getValidQTWI(mDAYS[i]))

    def create_month(self):
        if self.d == len(mDAYS):
            self.d = 0
        self.monthTW.clear()
        self.monthTW.setColumnCount(len(mDAYS))
        self.add_header_month()
        self.monthLabel.setText(self.month[0] + " " + unicode(self.year))
        self.monthTW.setRowCount(math.ceil((self.month[2] + self.d) * 1.0 / len(mDAYS)) + 1)
        self.days = []
        i = 0
        x = 1
        y = 0
        last_days = -1
        if self.d != 0:
            last_days = len(mDAYS) - self.d
            if self.month[1] > 1:
                last_dates = mMONTHS[self.month[1] - 1][2]
            else:
                last_dates = mMONTHS[(len(mMONTHS) - 1)][2]
            last_dates = range(last_dates - self.d, last_dates)

        all_days = self.month[2] + self.d
        next_days = len(mDAYS) - (all_days % len(mDAYS))
        all_days = next_days + all_days
        while i in range(all_days):
            if y > (len(mDAYS) - 1):
                x += 1
                y = 0
            daywidget = QWidget()
            layout = QBoxLayout(2, daywidget)
            daywidget.setLayout(layout)
            if i < self.d:
                if self.month[1] > 1:
                    daylabel = QLabel(unicode(last_dates[i] + 1) + "." + unicode(mMONTHS[self.month[1] - 1][1]) + "." + unicode(self.year))
                    daylabel.setStyleSheet("QLabel { color : gray; }")
                else:
                    daylabel = QLabel(unicode(last_dates[i] + 1) + "." + unicode(mMONTHS[(len(mMONTHS) - 1)][1]) + "." + unicode(self.year))
                    daylabel.setStyleSheet("QLabel { color : gray; }")
            elif i >= all_days - next_days:
                if all_days - i == len(mDAYS):
                    return
                if self.month[1] < (len(mMONTHS) - 1):
                    daylabel = QLabel(unicode(i - self.month[2] - (self.d - 1)) + "." + unicode(mMONTHS[self.month[1] + 1][1]) + "." + unicode(self.year))
                    daylabel.setStyleSheet("QLabel { color : gray; }")
                else:
                    daylabel = QLabel(unicode(i - self.month[2] - (self.d - 1)) + "." + unicode(mMONTHS[1][1]) + "." + unicode(self.year))
                    daylabel.setStyleSheet("QLabel { color : gray; }")
            else:
                daylabel = QLabel(unicode(i - (self.d - 1)) + "." + unicode(self.month[1]) + "." + unicode(self.year))
            layout.addWidget(daylabel)
            self.days.append(daywidget)
            self.monthTW.setCellWidget(x, y, daywidget)
            y += 1
            i += 1

    def next_month(self):
        self.d = (self.month[2] + self.d) % len(mDAYS)
        if self.month[1] < (len(mMONTHS) - 1):
            self.month = mMONTHS[self.month[1] + 1]
        else:
            self.month = mMONTHS[1]
            self.year = self.year + 1
            if self.year % 4 == 0:
                mMONTHS[2][2] = 29
            else:
                mMONTHS[2][2] = 28

    def previous_month(self):
        if self.month[1] > 1:
            self.month = mMONTHS[self.month[1] - 1]
        else:
            self.month = mMONTHS[len(mMONTHS) - 1]
            self.year = self.year - 1
            if self.year % 4 == 0:
                mMONTHS[2][2] = 29
            else:
                mMONTHS[2][2] = 28
        self.d = len(mDAYS) - ((self.month[2] + (len(mDAYS) - self.d)) % len(mDAYS))

    @pyqtSignature("")
    def on_nextB_clicked(self):
        self.next_month()
        self.create_month()

    @pyqtSignature("")
    def on_previousB_clicked(self):
        self.previous_month()
        self.create_month()

    def on_monthTW_cellDoubleClicked(self, x, y):
        widget = self.monthTW.cellWidget(x, y)
        if widget is None:
            return

        date = widget.findChildren(QLabel)[0].text()
        day = mDAYS[x]

        edit = Edit(self.c, self.conn, day, date, self)
        ret = edit.exec_()
        if ret == QDialog.Accepted:
            self.conn.commit()
        else:
            self.conn.rollback()
