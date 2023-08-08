list_1=[]
n = int (input("Введите количество элементов: "))
from random import randint
for i in range(n):
    list_1.append(randint(0,100))
print(list_1)
list_2=[]
min = int(input("Введите минимальное значение диапозона: "))
max = int(input("Введите максимальное значение диапозона: "))
for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
        list_2.append(i)
print(list_2)