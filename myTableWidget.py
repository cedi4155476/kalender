from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyTableWidget(QTableWidget):
    """
    add drag functionality to table
    """

    def __init__(self, parent=None):
        QTableWidget.__init__(self)
