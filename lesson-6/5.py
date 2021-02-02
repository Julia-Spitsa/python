class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Пишу слова')


class Pencil(Stationery):
    def draw(self):
        print('Делаю набросок')


class Marker(Stationery):
    def draw(self):
        print('Крашу ярко')


p = Pen('Ручка')
print(f'Я {p.title} -')
p.draw()
c = Pencil('Карандаш')
print(f'Я {c.title} -')
c.draw()
m = Marker('Маркер')
print(f'Я {m.title} -')
m.draw()

