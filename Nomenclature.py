class Unit():
  def __init__(self, id, subdivId, position, descr, form, count):
    self.id = id
    self.subdivId = subdivId
    self.position = position
    self.descr = descr
    self.form = {'1': 0, '2': 0, '3': 0}
    self.form[str(form)] = count

  def getFormStr(self):
    res = ""
    for key, val in self.form.items():
      if val > 0:
        res += f"{key} - {val} employeers"
    return res


class Nomenclature():
  def __init__(self):
    self.subdivision = {}
    self.units = []

  def addUnit(self, id, subdivId, position, descr, form, count):
    self.units.append(Unit(id, subdivId, position, descr, form, count))

  def show(self):
    for key, u in enumerate(self.units):
      print(f"id: {key}")
      print(f"position: {u.position}\n" \
            f"description: {u.descr}\n" \
            f"form: {u.getFormStr()}")

#class testing
if __name__ == "__main__":
  n = Nomenclature()
  n.addUnit(1, 1, "director", "main on factory", 2, 1)
  n.addUnit(2, 1, "engineer", "brain on factory", 2, 3)
  n.show()

