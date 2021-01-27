total_salary = 0
count = 0
with open('file3.txt', 'r', encoding="utf-8") as f:
    for line in f:
        data = line.split()
        surname, salary = data[0], float(data[1])
        total_salary += salary
        count += 1
        if salary < 20000:
            print(surname)
print(f'Средняя зарплата равна {round(total_salary/count, 2)} руб.')
