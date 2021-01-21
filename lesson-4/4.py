numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
gen = [el for el in numbers if numbers.count(el) == 1]
print(gen)
