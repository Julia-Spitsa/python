n = int(input('Введите количество секунд: '))
hour = n//3600
minute = (n % 3600)//60
sec = (n % 3600) % 60
print(f'Время: {hour:02}:{minute:02}:{sec:02}')
