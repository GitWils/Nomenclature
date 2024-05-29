#! /usr/bin/python3
import sys
from PyQt6 import QtGui, QtWidgets, QtCore
from DBManager import DBManager
from Nomenclature import Nomenclature
from pprint import pprint

class Project():
  def __init__(self):
    app = QtWidgets.QApplication(sys.argv)
    self.db = DBManager()
    self.db.getNomenclatureUnits()

  def showAll(self):
    print("TODO: showing all nomenclature units...")

def main():
  pr = Project()
  pr.showAll()

if __name__ == '__main__':
  main()
