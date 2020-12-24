n = int(input('Введите количество секунд: '))
hour = str(n//3600)
minute = str((n % 3600)//60)
sec = str((n % 3600) % 60)
print(f'Время: {hour}:{minute}:{sec}')

