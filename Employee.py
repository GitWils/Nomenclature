class Employee():
  def __init__(self, name, surname, form):
    self.name = name
    self.surname = surname
    self.form = form

  def show(self):
    print(self.name + " " + self.surname + " форма допуску - " + str(self.form))


#class testing
if __name__ == "__main__":
  empl1 = Employee("Юрій", "Рябченко", 2)
  empl1.show()

