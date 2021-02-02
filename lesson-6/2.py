class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calculation(self):
        weight = 25
        high = 5
        calc = (self._lenght * self._width * weight * high) / 1000
        print(f'{calc} т')


r_1 = Road(20, 5000)
r_1.calculation()
