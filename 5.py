earnings = int(input('Введите сумму выручки: '))
cost = int(input('Введите сумму издержек: '))
if earnings >= cost:
    profit = (earnings - cost)
    rent = (profit / earnings)
    print(f'Прибыль\nРентабельность: {rent}')
    count_person = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль на одного сотрудника: {profit/count_person}')
else:
    print('Убыток')


