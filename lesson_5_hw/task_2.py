'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
from collections import deque
from collections import Counter

MAXX = 16
SYMBOLS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

num_1 = deque(input('Введите первое число: '))
num_2 = deque(input('Введите второе число: '))

# num_1 = deque('A2')
# num_2 = deque('C4F')

while len(num_1) != len(num_2):
    if len(num_1) < len(num_2):
        num_1.appendleft('0')
    elif len(num_1) > len(num_2):
        num_2.appendleft('0')

print(num_1)
print(num_2)

num_1_num = [SYMBOLS[i] for i in num_1 if i in SYMBOLS]
num_2_num = [SYMBOLS[i] for i in num_2 if i in SYMBOLS]

print(num_2_num)
print(num_1_num)

spam = 0
res = deque()
for i in range(len(num_1_num) + 1):
    if i == 0:
        continue
    summ = num_1_num[-i] + num_2_num[-i] + spam
    if summ >= MAXX:
        res.appendleft(summ % MAXX)
        spam = 1
    else:
        res.appendleft(summ)
        spam = 0
else:
    if spam == 1:
        res.appendleft(1)

result = deque()
counter = 0

for i in num_1_num[::-1]:  # [10, 2] -> [2, 10]
    reso = {}
    for j in num_2_num[::-1]:  # [12, 4, 15] -> [15, 4, 12]

        mult = j * i
        counter += 1
        reso.update({str(counter): mult})

    counter = 0
    counter += 1
    result.append(reso)
print(result)

#########################
# res = deque()
# spam = 0
# result = []
#
# for i in num_1_num[::-1]:  # [10, 2] -> [2, 10]
#
#     for j in num_2_num[::-1]:  # [12, 4, 15] -> [15, 4, 12]
#         mult = j * i + spam
#         if mult >= MAXX:
#             res.appendleft(mult % MAXX)
#
#             spam = mult // MAXX
#         else:
#             res.appendleft(mult)
#             spam = 0
#     else:
#         if spam > 0:
#             res.appendleft(spam)
#     spam = 0
#
#     result.append(res)
#     res = deque()
#
# print(result)
#########################

print(res)

result = []

for i in res:
    for key, value in SYMBOLS.items():
        if i == value:
            result.append(key)

print(result)
