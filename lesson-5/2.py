with open('file2', 'r') as f:
    count = 0
    for line in f:
        print(line, end=' ')
        words = line.split()
        print('Количество слов: ', len(words))
        count += 1
print('Количество строк', count)
