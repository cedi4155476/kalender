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
from character import Character

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
        self.initialisedcharacters = False
        self.on_tabWidget_currentChanged(self.tabWidget.currentIndex())

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
            self.add_story()
        elif action.whatsThis() == "addcharacter":
            self.add_character()

    def on_tabWidget_currentChanged(self, tab):
        if tab == 0:
            if not self.initialisedstories:
                self.initialise_stories()
            self.create_stories()

        elif tab == 1:
            if not self.initialisedcharacters:
                self.initialise_characters()
            self.create_characters()

        elif tab == 2:
            if not self.initialisedmonth:
                self.initialise_month()
            self.create_month()

    def initialise_stories(self):
        self.c.execute('''SELECT id, titel, kurzinfo, pfad FROM Geschichte''')
        self.storydatas = self.c.fetchall()
        self.initialisedstories = True

    @pyqtSignature("")
    def on_storycreatePB_clicked(self):
        self.add_story()

    def create_stories(self):
        i = 0
        self.editbuttons = {}
        self.deletebuttons = {}
        self.storyTW.setRowCount(0)  # Refresh table
        self.storyTW.setRowCount(len(self.storydatas))
        for story in self.storydatas:
            editwidget = QWidget()
            editlayout = QBoxLayout(2, editwidget)
            editwidget.setLayout(editlayout)
            editbutton = QPushButton("Bearbeiten")
            editbutton.clicked.connect(self.edit_story)
            editlayout.addWidget(editbutton)
            self.editbuttons.setdefault(editbutton, [i, story['id']])

            deletewidget = QWidget()
            deletelayout = QBoxLayout(2, deletewidget)
            deletewidget.setLayout(deletelayout)
            deletebutton = QPushButton("Löschen")
            deletebutton.clicked.connect(self.delete_story)
            deletelayout.addWidget(deletebutton)
            self.deletebuttons.setdefault(deletebutton, [i, story['id']])

            self.storyTW.setItem(i, 0, self.getValidQTWI(unicode(story['titel'])))
            self.storyTW.setItem(i, 1, self.getValidQTWI(unicode(story['kurzinfo'])))
            self.storyTW.setItem(i, 2, self.getValidQTWI("Datei"))
            self.storyTW.setCellWidget(i, 3, editwidget)
            self.storyTW.setCellWidget(i, 4, deletewidget)
            i += 1

    def add_story(self):
        story = Story(False, self.c, self.conn, self)
        ret = story.exec_()
        if ret == QDialog.Accepted:
            self.conn.commit()
            self.initialise_stories()
            self.create_stories()
        else:
            self.conn.rollback()

    def delete_story(self):
        id = self.deletebuttons[self.sender()][1]
        self.c.execute('''DELETE FROM Geschichte WHERE id = {id}'''.format(id=id))
        self.c.fetchone()
        self.conn.commit()
        self.initialise_stories()
        self.storyTW.removeRow(self.deletebuttons[self.sender()][0])

    def edit_story(self):
        id = self.editbuttons[self.sender()][1]
        self.c.execute('''SELECT id, titel, kurzinfo, pfad FROM Geschichte WHERE id = {id}'''.format(id=id))
        story = Story(self.c.fetchone(), self.c, self.conn, self)
        ret = story.exec_()
        if ret == QDialog.Accepted:
            self.conn.commit()
            self.initialise_stories()
            self.create_stories()
        else:
            self.conn.rollback()

    def initialise_characters(self):
        self.c.execute('''SELECT id, vorname, nachname, geburtstag, info FROM Charakter''')
        self.characterdatas = self.c.fetchall()
        self.initialisedcharacters = True

    @pyqtSignature("")
    def on_charactercreatePB_clicked(self):
        self.add_character()

    def create_characters(self):
        i = 0
        self.editbuttons = {}
        self.deletebuttons = {}
        self.characterTW.setRowCount(0)  # Refresh table
        self.characterTW.setRowCount(len(self.characterdatas))
        for character in self.characterdatas:
            editwidget = QWidget()
            editlayout = QBoxLayout(2, editwidget)
            editwidget.setLayout(editlayout)
            editbutton = QPushButton("Bearbeiten")
            editbutton.clicked.connect(self.edit_character)
            editlayout.addWidget(editbutton)
            self.editbuttons.setdefault(editbutton, [i, character['id']])

            deletewidget = QWidget()
            deletelayout = QBoxLayout(2, deletewidget)
            deletewidget.setLayout(deletelayout)
            deletebutton = QPushButton("Löschen")
            deletebutton.clicked.connect(self.delete_character)
            deletelayout.addWidget(deletebutton)
            self.deletebuttons.setdefault(deletebutton, [i, character['id']])

            self.characterTW.setItem(i, 0, self.getValidQTWI(unicode(character['vorname'])))
            self.characterTW.setItem(i, 1, self.getValidQTWI(unicode(character['nachname'])))
            self.characterTW.setItem(i, 2, self.getValidQTWI(unicode(character['geburtstag'])))
            self.characterTW.setItem(i, 3, self.getValidQTWI(unicode(character['info'])))
            self.characterTW.setCellWidget(i, 4, editwidget)
            self.characterTW.setCellWidget(i, 5, deletewidget)
            i += 1

    def add_character(self):
        character = Character(False, self.c, self.conn, self)
        ret = character.exec_()
        if ret == QDialog.Accepted:
            self.conn.commit()
            self.initialise_characters()
            self.create_characters()
        else:
            self.conn.rollback()

    def delete_character(self):
        id = self.deletebuttons[self.sender()][1]
        self.c.execute('''DELETE FROM Charakter WHERE id = {id}'''.format(id=id))
        self.c.fetchone()
        self.conn.commit()
        self.initialise_characters()
        self.characterTW.removeRow(self.deletebuttons[self.sender()][0])

    def edit_character(self):
        id = self.editbuttons[self.sender()][1]
        self.c.execute('''SELECT id, vorname, nachname, geburtstag, info FROM Charakter WHERE id = {id}'''.format(id=id))
        character = Character(self.c.fetchone(), self.c, self.conn, self)
        ret = character.exec_()
        if ret == QDialog.Accepted:
            self.conn.commit()
            self.initialise_characters()
            self.create_characters()
        else:
            self.conn.rollback()

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
                    date = unicode(last_dates[i] + 1) + "." + unicode(mMONTHS[self.month[1] - 1][1]) + "." + unicode(self.year)
                    daylabel = QLabel(date)
                    daylabel.setStyleSheet("QLabel { color : gray; }")
                else:
                    date = unicode(last_dates[i] + 1) + "." + unicode(mMONTHS[(len(mMONTHS) - 1)][1]) + "." + unicode(self.year)
                    daylabel = QLabel(date)
                    daylabel.setStyleSheet("QLabel { color : gray; }")
            elif i >= all_days - next_days:
                if all_days - i == len(mDAYS):
                    return
                if self.month[1] < (len(mMONTHS) - 1):
                    date = unicode(i - self.month[2] - (self.d - 1)) + "." + unicode(mMONTHS[self.month[1] + 1][1]) + "." + unicode(self.year)
                    daylabel = QLabel(date)
                    daylabel.setStyleSheet("QLabel { color : gray; }")
                else:
                    date = unicode(i - self.month[2] - (self.d - 1)) + "." + unicode(mMONTHS[1][1]) + "." + unicode(self.year)
                    daylabel = QLabel(date)
                    daylabel.setStyleSheet("QLabel { color : gray; }")
            else:
                date = unicode(i - (self.d - 1)) + "." + unicode(self.month[1]) + "." + unicode(self.year)
                daylabel = QLabel(date)

            self.c.execute('''SELECT tag, notiz FROM Notiz''')
            notizen = self.c.fetchall()
            for notiz in notizen:
                if date == notiz['tag']:
                    if notiz['notiz'] == "Geburt":
                        daylabel.setStyleSheet("QLabel { color : red; }")
                    else:
                        daylabel.setStyleSheet("QLabel { color : blue; }")
            self.c.execute('''SELECT geburtstag FROM Charakter''')
            characters = self.c.fetchall()
            for character in characters:
                bd = character['geburtstag']
                cday, cmonth, cyear = bd.split('.')
                day, month, year = date.split('.')
                if year > cyear:
                    if (cday + "." + cmonth) == (day + "." + month):
                        daylabel.setStyleSheet("QLabel { color : green; }")

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
        self.conn.commit()
