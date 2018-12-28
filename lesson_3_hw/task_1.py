'''
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны любому из чисел в диапазоне от 2 до 9.
'''
import random

SIZE = 10
min_item = 2
max_item = 99
mult_start = 2
mult_end = 9

# тут вот вопрос: стоит ли обзывать стартовые переменные тут как константа?

array = [random.randint(min_item, max_item) for _ in range(SIZE)]
print(array)
print()            # этот принт для красоты

for mult in range(mult_start, mult_end+1):
    count = 0
    for i in array:
        if i % mult == 0:
            count += 1
    print(f'Чисел, кратных {mult}: {count}')

