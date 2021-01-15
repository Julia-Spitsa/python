def my_func(a, b, c):
    if a <= b and a <= c:
        res = b+c
        return res
    elif b <= a and b <=c:
        res = a+c
        return res
    else:
        res = b + a
        return res


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
print(my_func(a, b, c))
