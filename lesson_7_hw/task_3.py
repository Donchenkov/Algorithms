'''
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
равные части: в одной находятся элементы, которые не меньше медианы, в другой –
не больше медианы. Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не
рассматривался на уроках.
'''

import random


def median(array):
    for i in range(len(array)):
        cnt_less = 0
        cnt_more = 0
        cnt_equal = 0

        for j in range(len(array)):
            if j == i:
                continue
            elif array[j] < array[i]:
                cnt_less += 1
            elif array[j] > array[i]:
                cnt_more += 1
            else:
                cnt_equal += 1

        if cnt_less == cnt_more + cnt_equal or \
                cnt_more == cnt_less + cnt_equal or \
                cnt_less == cnt_more == cnt_equal:
            return f'median = {array[i]}'


m = 3  # не стал делать input и проверку на натуральность числа

array = [random.randint(0, 10) for i in range(2 * m + 1)]
print(array)

print(median(array))
