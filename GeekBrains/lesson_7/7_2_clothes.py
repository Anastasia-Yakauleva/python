"""Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""
from abc import ABC, abstractmethod


class Clothes(ABC):
    full_s = 0

    def __init__(self, size):
        self.size = size
        Clothes.full_s += self.square

    @property
    @abstractmethod
    def square(self):
        pass

    """def __add__(self, other):   
        return Clothes(self.square + other.square)"""

    def __str__(self):
        return f'Full square is {Clothes.full_s}'


class Coat(Clothes):
    @property
    def square(self):
        return round(self.size / 6.5 + 0.5)


class Costume(Clothes):
    @property
    def square(self):
        return round(self.size * 2 + 0.3)


coat = Coat(44)
jacket = Costume(44)
print(coat.square)
print(jacket.square)
print(Clothes.full_s)
