'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
позицию в массиве.
'''

import random

SIZE = 10
max_item = -750
min_item = -800
array = [random.randint(min_item, max_item) for _ in range(SIZE)]
print(array)

mx_mn_elem = float('-inf')

for i in range(len(array)):
    if mx_mn_elem < array[i] < 0:
        mx_mn_elem = array[i]
        index = i

if mx_mn_elem != float('-inf'):
    print(f'Максимальный отрицательный элемент в массиве: {index}; значение: {mx_mn_elem}')
