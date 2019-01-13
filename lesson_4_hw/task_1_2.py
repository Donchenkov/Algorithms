'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
элементами. Сами минимальный и максимальный элементы в сумму не включать.
'''
# import cProfile
import random


def sum_btw_w_minmax(size, max_item):
    count = 0

    array = [random.randint(0, max_item) for _ in range(size)]

    mx = max(array)
    mn = min(array)
    mx_idx = array.index(mx)
    mn_idx = array.index(mn)

    for i in range(len(array)):
        if mn_idx < i < mx_idx or mn_idx > i > mx_idx:
            count += array[i]

    if count > 0:
        return f'max = {array[mx_idx]}, min = {array[mn_idx]}\n' \
               f'Сумма эмементом между min и max: {count}'
    else:
        return f'max = {array[mx_idx]}, min = {array[mn_idx]}\n' \
               f'Между максимальным и минимальным элементомами нет элементов'

# cProfile.run('sum_btw_w_minmax(10000, 100)')
# 1    0.000    0.000    0.001    0.001 task_1_2.py:5(sum_btw_w_minmax) - 100, 100
# 1    0.005    0.005    0.036    0.036 task_1_2.py:8(<listcomp>) - 10000, 100
# 1    0.203    0.203    4.206    4.206 task_1_2.py:5(sum_btw_w_minmax) - 1000000, 100


# 100 loops, best of 5: 270 usec per loop - 100, 100
# 100 loops, best of 5: 26.6 msec per loop - 10000, 100
# 100 loops, best of 5: 53.7 msec per loop - 20000, 100
# 100 loops, best of 5: 139 msec per loop - 50000, 100
# 100 loops, best of 5: 289 msec per loop - 100000, 100
# 100 loops, best of 5: 1.42 sec per loop - 500000, 100

'''
Данный алгоритм (второй) как и первый имеет линейную сложность алгоритма. 
По поему предположению его сложность оценивается в O(n) * 5 за счет использования функций min(), max(), index().
Но по непонятной мне причине не смотря на то, что сложность данного алгоритма выше чем в первом примере, скорость 
немного выше. На мой взгля 23 строка замедляет работу алгоритма, тк приходится бежать по всему массиву, но строка 25 
в отличие от метода append() дает незначительную прибавку в скорости (во всяком случае в данном примере).
Среди остальных алгоритмов оказался средним по скорости.
'''