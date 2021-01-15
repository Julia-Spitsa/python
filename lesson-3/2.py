def func(name, surname, birth_year, city, email, phone):
    print(f'Имя: {name}, фамилия: {surname}, год рождения: {birth_year}, город проживания: {city}, '
          f'email: {email}, телефон: {phone}')


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
birth_year = input("Введите год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите email: ")
phone = input("Введите номер телефона: ")

func(name=name, surname=surname, birth_year=birth_year, city=city, email=email, phone=phone)
