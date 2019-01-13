'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования Решета Эратосфена;
'''


import cProfile

def prime_num(num):
    prime_lst = [2, ]
    i = 3

    while len(prime_lst) < num:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_lst += [i]
        i += 2

    return prime_lst[-1]


# 100 loops, best of 5: 2.56 msec per loop - 100
# 100 loops, best of 5: 113 msec per loop - 500
# 100 loops, best of 5: 527 msec per loop - 1000

cProfile.run('prime_num(500)')
# 1    0.002    0.002    0.002    0.002 task_2_1.py:10(prime_num) - 100
# 1    0.110    0.110    0.110    0.110 task_2_1.py:10(prime_num) - 500
# 1    0.534    0.534    0.535    0.535 task_2_1.py:10(prime_num) - 1000

# print(prime_num(2000))

'''
По всей видимости данный алгоритм пробегается по массиву каждый раз пока не найдет нужное искомое значение.
и чем больше искомое значение. Поправьте меня если я не прав но сложность данного алгоритма O(n^n) 
'''