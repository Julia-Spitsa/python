n = int(input('Введите положительное число: '))
max_num = 0
while n > 0:
    cur_numb = n % 10
    if max_num < cur_numb:
        max_num = cur_numb
    n //= 10
print(f'Максимальное число: {max_num}')
