'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random

SIZE = 100
max_item = 100
mn_index = 0
mx_index = 0

array = [random.randint(0, max_item) for _ in range(SIZE)]
print(array)

for i in range(len(array)):
    if array[i] < array[mn_index]:
        mn_index = i
    elif array[i] > array[mx_index]:
        mx_index = i

print(f'max = {array[mx_index]}, min = {array[mn_index]}')

array[mn_index], array[mx_index] = array[mx_index], array[mn_index]
print(array)
