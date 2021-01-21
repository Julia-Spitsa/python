my_list = input("Введите слова через пробел ")
my_words = []
num = 1
for el in range(my_list.count(' ') + 1):
    my_words = my_list.split()
    if len(str(my_words)) <= 10:
        print(f"{num} {my_words [el]}")
        num += 1
    else:
        print(f"{num} {my_words [el] [0:10]}")
        num += 1