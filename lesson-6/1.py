import time
from turtle import color


class TrafficLight:

    def __init__(self):
        self.__color = color

    def running(self):
        while True:
            self.__color = 'Red'
            print(self.__color)
            time.sleep(7)
            self.__color = 'Yellow'
            print(self.__color)
            time.sleep(2)
            self.__color = 'Green'
            print(self.__color)
            time.sleep(11)


T_l = TrafficLight()
T_l.running()
