import random

n = int(input("Введите кол-во кустов: "))
berries = list()
for i in range(n):
    berries.append(random.randint(1, 15))
print(berries)
max_sum = 0
for i in range(n):
    if max_sum < berries[i - 1] + berries[i] + berries[(i + 1) % n]:
        max_sum = berries[i - 1] + berries[i] + berries[(i + 1) % n]
print(max_sum)
