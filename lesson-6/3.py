class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        inc = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = inc


class Position(Worker):

    def get_full_name(self):
        full_name = self.name + " " + self.surname
        print(full_name)

    def get_total_income(self):
        total_income = self._income.get("wage") + self._income.get("bonus")
        print(f'Income {total_income}')


w_1 = Position("John", 'Smith', 'Manager', 5000, 700)
w_1.get_full_name()
w_1.get_total_income()
