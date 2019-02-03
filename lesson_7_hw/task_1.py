import random

'''
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100). 
Выведите на экран исходный и отсортированный массивы. 
Сортировка должна быть реализована в виде функции. 
По возможности доработайте алгоритм (сделайте его умнее).
'''


def bubble_sort(arr):
    n = 1

    while n < len(arr):
        tmp = 0
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                tmp += 1
        if tmp == 0:
            return array

        n += 1

        # print(arr)  # этот принт для наглядности


array = [random.randint(-100, 99) for i in range(10)]
print(f'Before bubbled: {array}')

bubble_sort(array)
print(f'After bubbled: {array}')
