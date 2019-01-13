'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Использовать алгоритм решето Эратосфена
'''


# import cProfile

def prime_eratosfen(num):
    n = int(num ** 1.5)
    sieve = [i for i in range(n)]

    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]

    return result[num - 1]


# 100 loops, best of 5: 553 usec per loop - 100
# 100 loops, best of 5: 7.19 msec per loop - 500
# 100 loops, best of 5: 21.3 msec per loop - 1000
# 100 loops, best of 5: 279 msec per loop - 5000

# cProfile.run('prime_eratosfen(500)')
#   1    0.000    0.000    0.001    0.001 task_2_2.py:9(prime_eratosfen) - 100
#   1    0.009    0.009    0.012    0.012 task_2_2.py:9(prime_eratosfen) - 500
#   1    0.017    0.017    0.021    0.021 task_2_2.py:9(prime_eratosfen) - 1000

# print(prime_eratosfen(10000))

'''
Если я правильно понимаю то сложность алгоритма за счет самого решета и повторной пробежке за счет 24 строки составляет 
O(n) * 2. тем не менне алгоритм работает в десятки раз быстрее собственно написанного. Хотя график (построенный по 
# точкам) показывает что алгоритм не линейный и больше похож на квадратичный(?). Предполагаю квадратичность сложности 
алгоритма достигается за счет того что возвожу в степень входящее значение num...
'''
