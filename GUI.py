# -*- coding: utf-8 -*-
"""
Module implementing MainWindow.
"""
import sqlite3
import os.path
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui_GUI import Ui_MainWindow

MONTHS = [["None", 0, 0],
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
        self.initialise()
        self.create()

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

    def initialise(self):
        self.item = None
        self.d = 4
        self.month = MONTHS[9]
        self.year = 580

    def add_header(self):
        self.monthTW.setItem(0, 0, self.getValidQTWI("Montag"))
        self.monthTW.setItem(0, 1, self.getValidQTWI("Dienstag"))
        self.monthTW.setItem(0, 2, self.getValidQTWI("Mittwoch"))
        self.monthTW.setItem(0, 3, self.getValidQTWI("Donnerstag"))
        self.monthTW.setItem(0, 4, self.getValidQTWI("Freitag"))
        self.monthTW.setItem(0, 5, self.getValidQTWI("Samstag"))
        self.monthTW.setItem(0, 6, self.getValidQTWI("Sonntag"))

    def getValidQTWI(self, value):
        """
        Make a valid qtablewidgetitem so it doesn't crash if it's empty
        """
        if value:
            return QTableWidgetItem(value)
        else:
            return QTableWidgetItem()

    def create(self):
        if self.d == 7:
            self.d = 0
        self.monthTW.clear()
        self.monthTW.setColumnCount(7)
        self.monthTW.setRowCount(7)
        self.add_header()
        self.monthLabel.setText(self.month[0] + " " + unicode(self.year))
        self.days = []
        i = 0
        x = 1
        y = 0
        last_days = -1
        if self.d != 0:
            last_days = 7 - self.d
            if self.month[1] > 1:
                last_dates = MONTHS[self.month[1] - 1][2]
            else:
                last_dates = MONTHS[12][2]
            last_dates = range(last_dates - self.d, last_dates)

        all_days = self.month[2] + self.d
        next_days = 7 - (all_days % 7)
        all_days = next_days + all_days
        while i in range(all_days):
            if y > 6:
                x += 1
                y = 0
            daywidget = QWidget()
            layout = QBoxLayout(2, daywidget)
            daywidget.setLayout(layout)
            if i < self.d:
                if self.month[1] > 1:
                    daylabel = QLabel(unicode(last_dates[i] + 1) + "." + unicode(MONTHS[self.month[1] - 1][1]) + "." + unicode(self.year))
                    daylabel.setStyleSheet("QLabel { color : gray; }")
                else:
                    daylabel = QLabel(unicode(last_dates[i] + 1) + "." + unicode(MONTHS[12][1]) + "." + unicode(self.year))
                    daylabel.setStyleSheet("QLabel { color : gray; }")
            elif i >= all_days - next_days:
                if all_days - i == 7:
                    return
                if self.month[1] < 12:
                    daylabel = QLabel(unicode(i - self.month[2] - (self.d - 1)) + "." + unicode(MONTHS[self.month[1] + 1][1]) + "." + unicode(self.year))
                    daylabel.setStyleSheet("QLabel { color : gray; }")
                else:
                    daylabel = QLabel(unicode(i - self.month[2] - (self.d - 1)) + "." + unicode(MONTHS[1][1]) + "." + unicode(self.year))
                    daylabel.setStyleSheet("QLabel { color : gray; }")
            else:
                daylabel = QLabel(unicode(i - (self.d - 1)) + "." + unicode(self.month[1]) + "." + unicode(self.year))
            layout.addWidget(daylabel)
            self.days.append(daywidget)
            self.monthTW.setCellWidget(x, y, daywidget)
            y += 1
            i += 1

    def next_month(self):
        self.d = (self.month[2] + self.d) % 7
        if self.month[1] < 12:
            self.month = MONTHS[self.month[1] + 1]
        else:
            self.month = MONTHS[1]
            self.year = self.year + 1
            if self.year % 4 == 0:
                MONTHS[2][2] = 29
            else:
                MONTHS[2][2] = 28

    def previous_month(self):
        if self.month[1] > 1:
            self.month = MONTHS[self.month[1] - 1]
        else:
            self.month = MONTHS[12]
            self.year = self.year - 1
            if self.year % 4 == 0:
                MONTHS[2][2] = 29
            else:
                MONTHS[2][2] = 28
        self.d = 7 - ((self.month[2] + (7 - self.d)) % 7)

    @pyqtSignature("")
    def on_nextB_clicked(self):
        self.next_month()
        self.create()

    @pyqtSignature("")
    def on_previousB_clicked(self):
        self.previous_month()
        self.create()

    def on_monthTW_cellClicked(self, x, y):
        widget = self.monthTW.cellWidget(x, y)
        if widget is None:
            return

        print "works"
