'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
элементами. Сами минимальный и максимальный элементы в сумму не включать.
'''

# import cProfile
import random


def sum_btw(size, max_item):
    mn_index = 0
    mx_index = 0
    count_btw = 0

    array = [random.randint(0, max_item) for _ in range(size)]

    for i in range(len(array)):
        if array[i] < array[mn_index]:
            mn_index = i
        elif array[i] > array[mx_index]:
            mx_index = i

    for i in range(len(array)):
        if mn_index < i < mx_index or mn_index > i > mx_index:
            count_btw += array[i]

    if count_btw > 0:
        return f'max = {array[mx_index]}, min = {array[mn_index]}\n' \
               f'Сумма эмементом между min и max: {count_btw}'
    else:
        return f'max = {array[mx_index]}, min = {array[mn_index]}\n' \
               f'Между максимальным и минимальным элементомами нет элементов'


# cProfile.run('sum_btw(1000, 100)')
# 1    0.001    0.001    0.004    0.004 task_1_1.py:8(sum_btw) - 100, 100
# 1    0.005    0.005    0.041    0.041 task_1_1.py:8(sum_btw) - 10000, 100
# 1    0.498    0.498    4.071    4.071 task_1_1.py:8(sum_btw) - 1000000, 100


# 100 loops, best of 5: 281 usec per loop - 100, 100
# 100 loops, best of 5: 29.4 msec per loop - 10000, 100
# 100 loops, best of 5: 59.4 msec per loop - 20000, 100
# 100 loops, best of 5: 149 msec per loop - 50000, 100
# 100 loops, best of 5: 311 msec per loop - 100000, 100
# 100 loops, best of 5: 1.46 sec per loop - 500000, 100

'''
Данный алгоритм - первоначальный, сданный в ДЗ.
Очевидно, что сложность алгоритма линейная. По поему предположению его сложность оценивается в O(n) * 2.
На мой взгля 23 строка замедляет работу алгоритма, тк приходится бежать по всему массиву, но строка 25 в отличие от 
метода append() дает незначительную прибавку в скорости (во всяком случае в данном примере).
Среди остальных алгоритмов оказался самым медленным.
'''
