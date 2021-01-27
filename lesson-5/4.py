translation = {"One": 'Один', "Two": 'Два', "Three": 'Три', "Four": 'Четыре', }
with open('file4_new.txt', 'w', encoding="utf-8") as f_new:
    with open('file4.txt', 'r', encoding="utf-8") as f:
        for line in f:
            data = line.split(' — ')
            eng, num = data[0], data[1]
            rus = translation.get(eng)
            print(f'{rus} — {num}', end='')
            f_new.write(f'{rus} — {num}')
