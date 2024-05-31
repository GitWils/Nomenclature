#! /usr/bin/python3
import sys
from PyQt6 import QtGui, QtWidgets, QtCore
from DBManager import DBManager
from Nomenclature import Nomenclature
from pprint import pprint

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pr = Project()
        self.setCentralWidget(self.pr)
        self.initUI()

    def initUI(self):
        """ user interface initialisation"""
        ico = QtGui.QIcon("img/logo.png")
        self.setWindowIcon(ico)
        self.setGeometry(50, 50, 974, 690)
        self.centerWindow()
        self.setWindowTitle('Штатний розпис')
        self.setMenuBar(self._createMenuBar())

    def _createMenuBar(self) -> QtWidgets.QMenuBar:
        """ top menu bar creating """
        menuBar = QtWidgets.QMenuBar(self)
        file_menu = QtWidgets.QMenu("&Файл", self)
        excellAct = QtGui.QAction("&Експорт в Excel", self)
        # excellAct.triggered.connect(self.pr.openSaveDlg)
        file_menu.addAction(excellAct)
        file_menu.addAction(QtGui.QAction("&Друк", self))
        view_menu = QtWidgets.QMenu("&Вигляд", self)
        view_menu.addAction(QtGui.QAction("&Налаштування", self))
        menuBar.addMenu(file_menu)
        menuBar.addMenu(view_menu)
        return menuBar

    def centerWindow(self):
        """ centering the main window in the center of the screen """
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def event(self, e) -> QtWidgets.QWidget.event:
        """ hotkey handling """
        if e.type() == QtCore.QEvent.Type.WindowDeactivate:
            self.setWindowOpacity(0.85)
        elif e.type() == QtCore.QEvent.Type.WindowActivate:
            self.setWindowOpacity(1)
        elif e.type() == QtCore.QEvent.Type.KeyPress and e.key() == QtCore.Qt.Key.Key_Escape:
            self.close()
        return QtWidgets.QWidget.event(self, e)

class Project(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.db = DBManager()
        self.db.getNomenclatureUnits()

        self.tableLayout = QtWidgets.QGridLayout()
        self.nomenclatureTbl = Nomenclature(self.db.getNomenclatureUnits())
        self.tableLayout.addWidget(self.nomenclatureTbl)
        self.setLayout(self.tableLayout)

    def showAll(self):
        # "TODO: showing all nomenclature units...")
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    ico = QtGui.QIcon("img/logo.png")
    app.setWindowIcon(ico)
    with open("style0.css", "r") as file:
        app.setStyleSheet(file.read())
    window = mainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()