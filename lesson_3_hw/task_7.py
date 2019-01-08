'''
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''

import random

SIZE = 10
max_item = 100
mn_index = 0
mn_index_sec = 0


array = [random.randint(0, max_item) for _ in range(SIZE)]
print(array)

for i in range(len(array)):
    if array[i] <= array[mn_index]:
        mn_index = i



