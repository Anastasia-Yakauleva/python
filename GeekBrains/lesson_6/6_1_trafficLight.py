"""Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный; в рамках метода реализовать переключение светофора в режимы:
красный, жёлтый, зелёный; продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод."""
from time import sleep


class TrafficLight:
    # атрибут
    __light_color = ["\u001b[41m\u001b[31;1m R \u001b[0m",
                     "\u001b[43m\u001b[33;1m Y \u001b[0m",
                     "\u001b[42m\u001b[32;1m G \u001b[0m"]  # background, text Color and reset with ANSI escape codes

    # метод
    def runing(self):
        print(TrafficLight.__light_color[0])
        sleep(7)  #
        print(TrafficLight.__light_color[1])
        sleep(2)
        print(TrafficLight.__light_color[2])
        sleep(2)


# объект
Kot_st = TrafficLight()
Kot_st.runing()
