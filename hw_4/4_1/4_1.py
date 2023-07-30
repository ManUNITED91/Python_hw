import random
set_1 = set()
set_2 = set()
n = int(input('Введите кол-чо элементов 1 списка: '))
m = int(input('Введите кол-чо элементов 2 списка: '))
for i in range(n):
    c = random.randint(1,10)
    set_1.add(c)   
print(set_1)
for i in range(m):
    c = random.randint(1,10)
    set_2.add(c)
print(set_2)
print(sorted(set_1.intersection(set_2)))