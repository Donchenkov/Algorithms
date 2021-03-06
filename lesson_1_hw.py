# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = int(input('Введите трехзначное число:'))

n1 = num // 100
n2 = num % 100 // 10
n3 = num % 10

num_sum = n1 + n2 + n3
num_mult = n1 * n2 * n3

print(f'Сумма цифр числа: {num_sum}')
print(f'Произведение цифр числа: {num_mult}')

# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# ​проходящей через эти точки.

x1 = int(input('Введите X1:'))
y1 = int(input('Введите Y1:'))
x2 = int(input('Введите X2:'))
y2 = int(input('Введите Y2:'))

k = (y1 - y2) / (x1 - x2)
b = y1 - (x1 * k)

print(f'Уравнение: y = {k}x + {b}')

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

letter1 = input('Введите первую букву:')
letter2 = input('Введите вторую букву:')

letter1_num = ord(letter1) - 96
letter2_num = ord(letter2) - 96
letters_btw = abs(letter1_num - letter2_num) - 1

print(f'Буква {letter1}: {letter1_num} по алфавиту')
print(f'Буква {letter2}: {letter2_num} по алфавиту')
print(f'Количество букв между буквами {letter1} и {letter2}: {letters_btw}')

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_num = int(input('Введите номер буквы в алфавите:'))

letter = chr(letter_num + 96)

print(f'{letter_num} буква алфавита: {letter}')

# 8. Определить, является ли год, который ввел пользователем, високосным или не високосным.

year = int(input('Введите год:'))

if year % 400 == 0:
    print(f'{year} год - високосный')
elif year % 100 == 0:
    print(f'{year} год - невисокосный')
elif year % 4 == 0:
    print(f'{year} год - високосный')
else:
    print(f'{year} год - невисокосный')

# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
c = int(input('Введите третье число'))

if a > c:
    if a < b:
        print(f'Среднее число: {a}')
    else:
        if b < c:
            print(f'Среднее число: {c}')
        else:
            print(f'Среднее число: {b}')
else:
    if a > b:
        print(f'Среднее число: {a}')
    else:
        if b > c:
            print(f'Среднее число: {c}')
        else:
            print(f'Среднее число: {b}')

