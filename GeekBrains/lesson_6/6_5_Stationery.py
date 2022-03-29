"""Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"\u001b[34mВы взяли ручку {self.title}\u001b[0m")


class Pencil(Stationery):
    def draw(self):
        print(f"\u001b[30;1mВы взяли карандаш {self.title}\u001b[0m")


class Handle(Stationery):
    def draw(self):
        print(f"\u001b[43m \u001b[30mВы взяли маркер {self.title}\u001b[0m")


pen = Pen("parker")
pen.draw()

pencil = Pencil("Oz")
pencil.draw()

h = Handle("Berlingo")
h.draw()
