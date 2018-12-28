'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
элементами. Сами минимальный и максимальный элементы в сумму не включать.
'''

import random

SIZE = 100
max_item = 100
mn_index = 0
mx_index = 0
count_btw = 0

array = [random.randint(0, max_item) for _ in range(SIZE)]
print(array)

for i in range(len(array)):
    if array[i] < array[mn_index]:
        mn_index = i
    elif array[i] > array[mx_index]:
        mx_index = i
print(f'max = {array[mx_index]}, min = {array[mn_index]}')

for i in range(len(array)):
    if mn_index < i < mx_index or mn_index > i > mx_index:
        count_btw += array[i]

if count_btw > 0:
    print(f'Сумма эмементом между min и max: {count_btw}')
else:
    print('Между максимальным и минимальным элементомами нет элементов')
