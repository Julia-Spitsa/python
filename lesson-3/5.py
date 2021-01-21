summa = 0
stop = False
while True:
    str_num = input("Введите числа через пробел: ")
    current_num = '0'
    for sym in str_num:
        if sym == 'q':
            stop = True
            break
        elif sym != ' ':
            current_num += sym
        else:
            summa += int(current_num)
            current_num = '0'
    summa += int(current_num)
    print(summa)
    if stop:
        break
