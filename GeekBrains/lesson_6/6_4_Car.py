"""Реализуйте базовый класс Car.
Aтрибуты: speed, color, name, is_police (булево).
Mетоды: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
Дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости."""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} is moving!"

    def stop(self):
        return f"{self.name} stopped."

    def turn(self, direction):
        return f"{self.name} turned {direction}."

    def show_speed(self):
        return f"{self.name}`s speed is {self.speed}."


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            return f"{self.name}`s speed is {self.speed}."
        else:
            return "\u001b[31;1mThe speed limit has been exceeded!\u001b[0m"


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            return f"{self.name}`s speed is {self.speed}."
        else:
            return "\u001b[31;1mThe speed limit has been exceeded by {self.speed}!\u001b[0m"


class SportCar(Car):
    pass


class PoliceCar(Car):
    def polise(self):
        if self.is_police:
            return f"{self.name} is from the police department."
        else:
            return f"{self.name} is not from the police department."


shk = TownCar(66, "red", "Skoda", False)
print(shk.color)
print(shk.show_speed())
print(shk.turn("home"))

audy = SportCar(55, "green", "Audy", False)
print(audy.show_speed())

w3 = PoliceCar(132, "white", "Lada", True)
print(w3.polise())
print(w3.go())
print(w3.stop())
