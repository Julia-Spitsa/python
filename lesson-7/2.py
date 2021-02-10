from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, cloth):
        self.cloth = cloth

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return float(self.consumption) + float(other.consumption)


class Coat(Clothes):
    @property
    def consumption(self):
        return f'{self.cloth / 6.5 + 0.5:.2f}'


class Costume(Clothes):
    @property
    def consumption(self):
        return f'{2 * self.cloth + 0.3:.2f}'


coat = Coat(40)
costume = Costume(180)
print(f'Расход ткани на пальто: {coat.consumption}')
print(f'Расход ткани на костюм: {costume.consumption}')
print(f'Расход ткани суммарно: {coat + costume}')
