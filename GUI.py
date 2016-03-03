# -*- coding: utf-8 -*-
"""
Module implementing MainWindow.
"""
import sqlite3
import os.path
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui_GUI import Ui_MainWindow
from months import Month

MONTHS = [["None", 0, 0],
          ["Januar", 1, 31],
          ["Februar", 2, 28],
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
        self.days = []
        self.item = None
        self.d = 4

    def create(self, year=580, month=MONTHS[9]):

        self.month = month
        self.year = year
        self.monthLabel.setText(self.month[0] + " " + unicode(self.year))

        i = 0
        x = 1
        y = 0
        last_days = 0
        if self.d != 0:
            last = True
            last_days = 7 - self.d
        else:
            last = False
        all_days = self.month[2] + last_days + 1
        next_days = 7 - (all_days % 7)
        all_days = next_days + all_days
        while i in range(all_days):
            if last:
                last_dates = MONTHS[self.month[1] - 1][2]
                last_dates = range(last_dates - last_days, last_dates + 1)
                last = False

            if y > 6:
                x += 1
                y = 0
                last = False
            daywidget = QWidget()
            layout = QBoxLayout(2, daywidget)
            daywidget.setLayout(layout)
            if i <= last_days:
                daylabel = QLabel("<font color='Gray'>" + unicode(last_dates[i]) + "." + unicode(MONTHS[self.month[1] - 1][1]) + "." + unicode(self.year) + "</font>")
            elif i >= all_days - next_days:
                daylabel = QLabel("<font color='Gray'>" + unicode(i - self.month[2] - last_days) + "." + unicode(MONTHS[self.month[1] + 1][1]) + "." + unicode(self.year) + "</font>")
            else:
                daylabel = QLabel(unicode(i - last_days) + "." + unicode(self.month[1]) + "." + unicode(self.year))
            layout.addWidget(daylabel)
            self.days.append(daywidget)
            self.monthTW.setCellWidget(x, y, daywidget)
            y += 1
            i += 1

    @pyqtSignature("")
    def on_tableWidget_itemSelectionChanged(self):
        """
        change current editable
        """
        if self.tableWidget.selectedItems():
            self.item = self.tableWidget.selectedItems()[0]
