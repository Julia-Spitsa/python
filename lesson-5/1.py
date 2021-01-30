with open('file1.txt', 'w') as f:
    while True:
        line = input('Input line: ')
        if not line:
            break
        f.write(f'{line}\n')

