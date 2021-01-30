from sys import argv

def salary():
    try:
         hours, rate, bonus = map(float, argv[1:])
         print(f"Salary = {hours * rate + bonus}")
    except ValueError:
         print("Введите три числа ")


salary()
