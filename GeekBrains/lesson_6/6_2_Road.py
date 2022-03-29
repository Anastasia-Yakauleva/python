"""определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
проверить работу метода."""


class Road:

    def __init__(self, leng, width):
        self._length = leng
        self._width = width

    def asphalt_mass(self, weight, hight):
        print(
            f"{self._length}m * {self._width}m * {weight}kg/cm * {hight}cm ="
            f" {self._length * self._width * weight * hight / 1000}t.")


m6 = Road(5000, 20)
m6.asphalt_mass(25, 5)
