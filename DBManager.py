import sys
import datetime
from PyQt6 import QtCore, QtSql

from pprint import pprint


class CustomQuerry(QtSql.QSqlQuery):
    """ class used for catching sql errors """
    def __init__(self):
        super().__init__()

    def clear(self):
        error = self.lastError()
        if error.isValid():
            print(f"Помилка: {error.text()}")
        super().clear()

class DBManager():
    def __init__(self):
        self.con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.con.setDatabaseName('data.s')
        self.con.open()
        # self.query = QtSql.QSqlQuery()
        self.query = CustomQuerry()

        if 'subdivisions' not in self.con.tables():
            self.query.exec(" create table subdivisions(id integer primary key autoincrement, " +
                            " name text, str_date text, dt datetime, enable bool default true)")
            # self.checkerrors()
            self.query.clear()

        if 'units' not in self.con.tables():
            self.query.exec(" create table units(id integer primary key autoincrement, " +
                            " subdiv_id integer secondary key, position text, descr text, " +
                            " form_1 integer default 0, form_2 integer default 0, form_3 integer default 0, " +
                            " str_date text, dt datetime, enable bool default true)")
            # self.checkerrors()
            self.query.clear()

    def getNomenclatureUnits(self):
        self.query.exec(" select units.position " +
                        " from units " +
                        " join subdivisions on " +
                        " (subdivisions.id = units.subdiv_id) " +
                        " order by units.id ")
        lst = []
        if self.query.isActive():
            self.query.first()
            while self.query.isValid():
                arr = dict({
                    'id': self.query.value('id'),
                    'position': self.query.value('name')})
                lst.append(arr)
                self.query.next()
        # self.checkerrors()
        self.query.clear()
        return lst

    # def saveNomenclatureUnit(self, name, items):
    #     date = self.getDateTime()
    #     self.query.prepare("insert into templates values(null, :name, True, :str_date, :dt, True)")
    #     self.query.bindValue(':name', name)
    #     self.query.bindValue(':str_date', date['s_date'])
    #     self.query.bindValue(':dt', date['datetime'])
    #     self.query.exec()
    #     templateId = self.query.lastInsertId()
    #     self.query.clear()
    #     for item in items:
    #         self.query.prepare("insert into items_template values(null, :template_id, :name, :count, 1, True, :str_date, :dt, True)")
    #         self.query.bindValue(':template_id', templateId)
    #         self.query.bindValue(':name', item['name'])
    #         self.query.bindValue(':count', item['count'])
    #         self.query.bindValue(':str_date', date['s_date'])
    #         self.query.bindValue(':dt', date['datetime'])
    #         self.query.exec()
    #         self.query.clear()

    def getDateTime(self):
        date = datetime.datetime.now()
        res = dict({'s_date': date.strftime("%H:%M %d.%m.%Y"), 'datetime': str(date)})
        return res

    def checkerrors(self):
        error = self.query.lastError()
        if error.isValid():
            print(f"Помилка: {error.text()}")

    def __del__(self):
        pass
        # self.con.close()
