from PyQt6 import QtGui, QtWidgets, QtCore
from CustomWidgets import CustomTable
from datetime import datetime

class Unit():
    def __init__(self, id, subdivId, position, descr, form, count):
        self.id = id
        self.subdivId = subdivId
        self.position = position
        self.descr = descr
        self.form = {'1': 0, '2': 0, '3': 0}
        self.form[str(form)] = count

    def getFormStr(self) -> str:
        res = ""
        for key, val in self.form.items():
            if val > 0:
                res += f"{key} - {val} employeers"
        return res


class Nomenclature(CustomTable):
    def __init__(self, units):
        QtWidgets.QTableView.__init__(self)
        self.subdivision = {}
        self.units = units
        self.sti = TableModel(units)
        self.loadData(self.units)

    def loadData(self, units):
        self.units = list(units)
        self.sti.clear()
        self.sti.setHorizontalHeaderLabels(
            ['Id', 'Порядковий\nномер', 'Найменування\nпідрозділу', 'Загальна кількість працівників\nпідрозділу',
             'Найменування посади\nпрацівника підрозділу', 'Обгрунтування\nнеобхідності надання доступу'])
        self.sti.setRowCount(5)
        proxy_model = CustomSortFilterProxyModel()
        proxy_model.setSourceModel(self.sti)
        self.setModel(proxy_model)
        self.setColumnStyles()

    def addUnit(self, id, subdivId, position, descr, form, count):
        self.units.append(Unit(id, subdivId, position, descr, form, count))

    # def show(self):
    #     for key, u in enumerate(self.units):
    #         print(f"id: {key}\n" \
    #               f"position: {u.position}\n" \
    #               f"description: {u.descr}\n" \
    #               f"form: {u.getFormStr()}")


    def setColumnStyles(self):
        CustomTable.setColumnStyles(self)
        header = self.horizontalHeader()
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.setSortingEnabled(True)
        #self.sortByColumn(2, QtCore.Qt.SortOrder.DescendingOrder)
        #header.setMaximumWidth(300)


class TableModel(QtGui.QStandardItemModel):
    """ class used for align and coloring cells  """
    def __init__(self, data, cntItems=0):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole and len(self._data):
            match index.column():
                case 0:
                    return self._data[index.row()]['id']
                case 1:
                    return self._data[index.row()]['name']
                case 2:
                    return self._data[index.row()]['template_name']
                case 3:
                    return self._data[index.row()]['completed']
                case 4:
                    return self._data[index.row()]['sended']
                case 5:
                    return self._data[index.row()]['count']
                case 6:
                    return self._data[index.row()]['date'][5:]
                case 7:
                    return self._data[index.row()]['note']
            return 1

        if (role == QtCore.Qt.ItemDataRole.BackgroundRole
                and len(self._data)
                and index.column() == 4
                and self._data[index.row()]['sended'] < self._data[index.row()]['count']):
            return QtGui.QColor(TableModel.getColorByRelative(float(self._data[index.row()]['sended'] / self._data[index.row()]['count'])))

        if (role == QtCore.Qt.ItemDataRole.TextAlignmentRole and index.column() != 1):
            return QtCore.Qt.AlignmentFlag.AlignCenter

    # def getSelectedName(self, index):
    #     return self._data[index.row()]['name']

    def getSelectedRow(self, index):
        return self._data[index.row()]['id']

    @staticmethod
    def getColorByRelative(val):
        """ takes float value from 0 to 1, returns string such as #ee5555 """
        return f"#ee{int(val * 200 + 55):02X}{int(val * 200 + 55):02X}"

    def reloadData(self, data):
        """ reload table data """
        self._data = list(data)


class CustomSortFilterProxyModel(QtCore.QSortFilterProxyModel):
    def lessThan(self, left_index, right_index):
        left_data = self.sourceModel().data(left_index, QtCore.Qt.ItemDataRole.DisplayRole)
        right_data = self.sourceModel().data(right_index, QtCore.Qt.ItemDataRole.DisplayRole)
        if left_data is None and right_data is None:
            return False
        elif left_data is None:
            return True
        elif right_data is None:
            return False
        else:
            # if (left_index.column() == 4):
            #     #removing suffix".шт"
            #     left_data = int(left_data[:-4])
            #     right_data = int(right_data[:-4])
            # #sorting date column
            if (left_index.column() == 6):
                left_data = datetime.strptime(left_data, " %d.%m.%Y").date()
                right_data = datetime.strptime(right_data, " %d.%m.%Y").date()
            return left_data > right_data


# class testing
if __name__ == "__main__":
    n = Nomenclature()
    n.addUnit(1, 1, "director", "main on the factory", 2, 1)
    n.addUnit(2, 1, "engineer", "brain on the factory", 2, 3)
    n.show()
