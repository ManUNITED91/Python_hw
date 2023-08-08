list_1 = []
a1 = int(input("Введите первый элемент арифметической проггрессии: "))
d = int (input ("Введите разность: "))
n = int(input ("Введите количество элементов: "))
for i in range(n):
    list_1.append(a1 + i*d)
print(list_1)