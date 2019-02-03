'''
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
отсортированный массивы.
'''
import random


def merge_sort(array):
    half_index = len(array) // 2
    if len(array) <= 1:
        return array

    left_side = merge_sort(array[:half_index])
    right_side = merge_sort(array[half_index:])

    return merge(left_side, right_side)


def merge(left_side, right_side):
    result = []

    while len(left_side) > 0 and len(right_side) > 0:
        if left_side[0] <= right_side[0]:
            result.append(left_side.pop(0))
        else:
            result.append(right_side.pop(0))

    if len(left_side) > 0:
        result += left_side
    if len(right_side) > 0:
        result += right_side
    return result


array = [round(random.triangular(-50, 49), 3) for i in range(10)]

print(f'Before merged: {array}')

new_array = merge_sort(array)
print(f'After merged: {new_array}')
