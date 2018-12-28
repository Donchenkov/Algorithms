'''
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
'''

import random

SIZE = 10
max_item = 100
result = []

array = [random.randint(0, max_item) for _ in range(SIZE)]
print(array)

for item in range(len(array)):
    if array[item] % 2 == 0:
        result += [array[item]]

print(result)
