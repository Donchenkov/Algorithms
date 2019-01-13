'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
элементами. Сами минимальный и максимальный элементы в сумму не включать.
'''
# import cProfile
import random
import functools


@functools.lru_cache()
# 100 loops, best of 5: 234 nsec per loop - 500000, 100
# 100 loops, best of 5: 287 nsec per loop - 1000000, 100

def sum_btw_w_sort(size, max_item):
    result = []

    array = [random.randint(0, max_item) for _ in range(size)]
    # Здесь замедление за счет sorted()
    srt_array = sorted(array)
    mx = srt_array[-1]
    mn = srt_array[0]
    mx_idx = array.index(mx)
    mn_idx = array.index(mn)

    if mn_idx > mx_idx:
        mn_idx, mx_idx = mx_idx, mn_idx

    # Тут идет ускорение за счет того что пробегаем только по нужному участку массивва почти на 10 %
    for i in range(mn_idx, mx_idx + 1):
        if mn_idx < i < mx_idx:
            result.append(array[i])

    if len(result) > 0:
        return f'max = {array[mx_idx]}, min = {array[mn_idx]}\n' \
               f'Сумма эмементом между min и max: {sum(result)}'
    else:
        return f'max = {array[mx_idx]}, min = {array[mn_idx]}\n' \
               f'Между максимальным и минимальным элементомами нет элементов'

# cProfile.run('sum_btw_w_sort(10000, 100)')
# 1    0.000    0.000    0.000    0.000 task_1_3.py:9(sum_btw_w_sort) - 100, 100
# 1    0.002    0.002    0.038    0.038 task_1_3.py:9(sum_btw_w_sort) - 10000, 100
# 1    0.220    0.220    4.419    4.419 task_1_3.py:9(sum_btw_w_sort) - 1000000, 100


# 100 loops, best of 5: 255 usec per loop - 100, 100
# 100 loops, best of 5: 26.3 msec per loop - 10000, 100
# 100 loops, best of 5: 53.3 msec per loop - 20000, 100
# 100 loops, best of 5: 135 msec per loop - 50000, 100
# 100 loops, best of 5: 270 msec per loop - 100000, 100
# 100 loops, best of 5: 1.37 sec per loop - 500000, 100

'''
Данный алгоритм (третий) как первый и второй имеет линейную сложность алгоритма. 
По поему предположению его сложность оценивается в O(n) * 4 за счет использования 
функций sorted(), append(), index(), sum().
Здесь в отличие от примера 2 - sorted() (19 строка) скушал время но мы нашли min и max всего за обход 
и съэкономили ресурсы. Также реализация суммирования чисел (29 строка) только нужного нам интервала 
(в отличие от примеров 1 и 2) не смотря на метод append() (31 строка) и метод sum() (35 строка) 
дала на прибавку почти в 10 %.    
Среди остальных алгоритмов оказался самым быстрым.
'''