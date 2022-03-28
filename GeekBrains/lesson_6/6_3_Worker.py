"""Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker; в классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров."""


class Worker:

    def __init__(self, name, surname, pos, wage, bonus):
        self.name = name
        self.surname = surname
        self.pos = pos
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, pos, wage, bonus):
        super().__init__(name, surname, pos, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


Anton = Position("Anton", "Kotov", "manager", 700, 300)
print(Anton.get_full_name())
print(Anton.get_total_income())
