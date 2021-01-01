year = {"зима": [12, 1, 2],
        "весна": [3, 4, 5],
        "лето": [6, 7, 8],
        "осень": [9, 10, 11]}
month = int(input("Введите целое число от 1 до 12: "))
while (month < 1) or (month > 12):
    month = int(input("Введите целое число от 1 до 12: "))
for season in year.keys():
    if month in year[season]:
        print(season)
        break
