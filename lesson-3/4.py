def my_func(x, y):
    res = x**y
    return res


def my_func2(x, y):
    res2 = 1
    count = 0
    while abs(y) > count:
        res2 *= 1/x
        count += 1
    return res2


x = int(input("Введите действительное положительное число: "))
while x < 0:
    print("Попробуйте еще раз")
    x = int(input("Введите действительное положительное число: "))
y = int(input("Введите степень: "))
while y >= 0:
    print("Попробуйте еще раз")
    y = int(input("Введите степень: "))
print(my_func(x, y))
print(my_func2(x, y))
