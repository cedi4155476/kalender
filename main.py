#! /usr/bin/python
import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from GUI import MainWindow


def launch():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    launch()
