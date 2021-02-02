class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print('Run')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print(f'Turn {direction}')

    def show_speed(self, speed):
        print(f'Current speed is {speed}')


class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print(f'Overspeed')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self, speed):
        if speed > 40:
            print(f'Overspeed')
        else:
            print(f'Current speed is {speed}')


class PoliceCar(Car):
    pass


work = WorkCar(50, 'red', 'Im', False)
print(f'Color is {work.color}')
print(f'Name is {work.name}')
print(f'Is car police? - {work.is_police}')
work.go()
work.show_speed(50)
work.turn('left')
work.stop()

police = PoliceCar(60, 'white', 'Pol', True)
print(f'Color is {police.color}')
print(f'Name is {police.name}')
print(f'Is car police? - {police.is_police}')
police.go()
police.show_speed(60)
police.turn('right')
police.stop()
