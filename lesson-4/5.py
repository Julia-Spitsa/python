from functools import reduce

gen = [el for el in range(100, 1001) if el % 2 == 0]
print(gen)

def multiple(a, b):
    return a * b


print(reduce(multiple, gen))
