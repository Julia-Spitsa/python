with open('file5.txt', 'w') as f:
    f.write('1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ')
with open('file5.txt', 'r') as f:
    numbers = f.readline()
    numbs = numbers.split()
    print(numbs)

summa = 0
for el in numbs:
    summa += int(el)

print(summa)
