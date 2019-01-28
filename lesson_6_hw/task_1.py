import sys

arr = [56, 78, 77, 36, 17, 93, 49, 86, 82, 85, 87, 17, 5]

def sum_btw(*array):
    mn_index = 0
    mx_index = 0
    count_btw = 0

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
               f'Сумма эмементом между min и max: {count_btw}', locals()
    else:
        return f'max = {array[mx_index]}, min = {array[mn_index]}\n' \
               f'Между максимальным и минимальным элементомами нет элементов', locals()


def show_size(x, level=0, sum_all=[]):
    if level == 2:
        print(f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
        sum_all.append(sys.getsizeof(x))

    if hasattr(x, '__iter__'):  # объект можно перебирать в цикле: список, кортеж, словарь, множество
        if hasattr(x, 'items'):
            for key, value in x.items():
                # show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)

    return sum(sum_all)


print(show_size(sum_btw(arr)))  # --> 1080

'''
64 разраядня ОС, Python 3.7.0

НАИБОЛЕЕ ЭФФЕКТИВНОЕ ИСПОЛЬЗОВАНИЕ ПАМЯТИ

type = <class 'tuple'>, size = 56, object = ([56, 78, 77, 36, 17, 93, 49, 86, 82, 85, 87, 17, 5],)
type = <class 'int'>, size = 24, object = 0
type = <class 'int'>, size = 24, object = 0
type = <class 'int'>, size = 24, object = 0
type = <class 'int'>, size = 24, object = 0
152
'''