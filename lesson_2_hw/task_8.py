'''
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''

# base = ''
# numbers = int(input('Сколько чисел вы хотите ввести:'))
# dig = int(input('Какую цифру ищем:'))
#
#
# for i in range(numbers):
#     num = int(input(f'Введите {i+1} число:'))
#     base += str(num)
#
# count = base.count(str(dig))
# print(f'Количество цифр {dig} в введнных числах: {count}')

count = 0
numbers = int(input('Сколько чисел вы хотите ввести:'))
dig = int(input('Какую цифру ищем:'))

for i in range(numbers):
    num = int(input(f'Введите {i+1} число: '))
    while num > 0:
        if num % 10 == dig:
            count += 1
        num = num // 10

print(f'Количество цифр {dig} в введнных числах: {count}')