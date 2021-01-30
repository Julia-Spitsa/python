def func(num1, num2):
    if num2 == 0:
        res = "На ноль делить нельзя"
    else:
        res = num1/num2
    return res


a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))
print(func(a, b))
