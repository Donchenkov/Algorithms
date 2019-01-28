import random
import sys

arr = [56, 78, 77, 36, 17, 93, 49, 86, 82, 85, 87, 17, 5]

def sum_btw_w_minmax(*array):
    count = 0

    mx = max(array)
    mn = min(array)
    mx_idx = array.index(mx)
    mn_idx = array.index(mn)

    for i in range(len(array)):
        if mn_idx < i < mx_idx or mn_idx > i > mx_idx:
            count += array[i]
    if count > 0:
        return f'max = {array[mx_idx]}, min = {array[mn_idx]}\n' \
               f'Сумма эмементом между min и max: {count}', locals()
    else:
        return f'max = {array[mx_idx]}, min = {array[mn_idx]}\n' \
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


print(show_size(sum_btw_w_minmax(arr)))      # --> 1136
'''
64 разраядня ОС, Python 3.7.0

type = <class 'tuple'>, size = 56, object = ([56, 78, 77, 36, 17, 93, 49, 86, 82, 85, 87, 17, 5],)
type = <class 'int'>, size = 24, object = 0
type = <class 'list'>, size = 168, object = [56, 78, 77, 36, 17, 93, 49, 86, 82, 85, 87, 17, 5]
type = <class 'list'>, size = 168, object = [56, 78, 77, 36, 17, 93, 49, 86, 82, 85, 87, 17, 5]
type = <class 'int'>, size = 24, object = 0
type = <class 'int'>, size = 24, object = 0
type = <class 'int'>, size = 24, object = 0
488
'''