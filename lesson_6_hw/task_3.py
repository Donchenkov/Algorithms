import sys

arr = [56, 78, 77, 36, 17, 93, 49, 86, 82, 85, 87, 17, 5]

def sum_btw_w_sort(*array):
    result = []

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
               f'Сумма эмементом между min и max: {sum(result)}', locals()
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
                #show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)

    return sum(sum_all)

print(show_size(sum_btw_w_sort(arr)))      # --> 2308

'''
type = <class 'tuple'>, size = 56, object = ([56, 78, 77, 36, 17, 93, 49, 86, 82, 85, 87, 17, 5],)
type = <class 'list'>, size = 64, object = []
type = <class 'list'>, size = 96, object = [[56, 78, 77, 36, 17, 93, 49, 86, 82, 85, 87, 17, 5]]
type = <class 'list'>, size = 168, object = [56, 78, 77, 36, 17, 93, 49, 86, 82, 85, 87, 17, 5]
type = <class 'list'>, size = 168, object = [56, 78, 77, 36, 17, 93, 49, 86, 82, 85, 87, 17, 5]
type = <class 'int'>, size = 24, object = 0
type = <class 'int'>, size = 24, object = 0
type = <class 'int'>, size = 24, object = 0
624
'''