import sys
from PyQt6 import QtGui, QtWidgets, QtCore

class CustomTable(QtWidgets.QTableView):
    def __init__(self):
        self.setColumnStyles()
        #self.setObjectName("table")


    def setColumnStyles(self):
        #self.setMinimumWidth(800)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.setAlternatingRowColors(True)
        self.setSortingEnabled(True)
        self.setEditTriggers(QtWidgets.QListView.EditTrigger.NoEditTriggers)
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.setColumnHidden(0, True)
        #header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)