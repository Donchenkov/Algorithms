'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
'''

rev_num = ''

num = int(input('Введите число для преобразования'))

while num > 0:
    dig = num % 10
    num = num // 10
    rev_num += str(dig)

print(rev_num)
