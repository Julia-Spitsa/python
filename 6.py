a = int(input('Введите результат первого дня: '))
b = int(input('Введите цель: '))
count = 1
while a < b:
    a *= 1.1
    count += 1
print(f'{count}-й день')


