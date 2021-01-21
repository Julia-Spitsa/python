from math import factorial

def generator():
    for el in range(1, 5):
        yield factorial(el)

g = generator()
print(g)
for el in g:
    print(el)
