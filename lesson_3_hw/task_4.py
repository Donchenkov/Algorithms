'''
Определить, какое число в массиве встречается чаще всего.
'''

import random

SIZE = 100
max_item = 10
array = [random.randint(1, max_item) for _ in range(SIZE)]
print(array)

mx_count = 0
rife_num = 0

for i in range(len(array)):
    count = 0
    for j in range(len(array)):
        if array[j] == array[i]:
            count += 1
    if count > mx_count:
        mx_count = count
        rife_num = array[i]

print(f'Число {rife_num} встречается {mx_count} раз(-а)')
