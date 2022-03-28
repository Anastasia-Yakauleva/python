"""Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker; в классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров."""


class Road:

    def __init__(self, len, width):
        self._length = len
        self._width = width

    def asphalt_mass(self, weight, hight):
        print(
            f"{self._length}m * {self._width}m * {weight}kg * {hight}cm ="
            f" {self._length * self._width * weight * hight / 1000}t.")


m6 = Road(5000, 20)
m6.asphalt_mass(25, 5)
