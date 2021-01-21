from itertools import count, cycle

for el in count(3):
    print(el)
    if el == 10:
        break

count = 0
for el in cycle([1, 3, 5]):
    print(el)
    count += 1
    if count > 5:
        break
