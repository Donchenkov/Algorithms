'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
'''

from collections import namedtuple

companies = []
total_profit = 0

companies_q = int(input('Введите количество компаний: '))

New_Company = namedtuple('New_Company', 'name profit year_profit')

for i in range(companies_q):
    profit = []
    year_profit = 0
    name = input(f'введите название {i+1} компании ')

    for j in range(4):
        profit += [int(input(f'прибыль за {j+1} картал: '))]
        year_profit += profit[j]

    print(f'Годовая прибыль: {year_profit}')
    total_profit += year_profit

    companies.append(New_Company(name, profit, year_profit))

av_profit = int(sum(i.year_profit for i in companies) / companies_q)

print(f'Среднегодовая прибыль всех компаний: {av_profit}')

less_av = list(i.name for i in companies if i.year_profit < av_profit)
more_av = list(i.name for i in companies if i.year_profit > av_profit)

print(f'Компании с прибылью ниже среденей: {less_av}')
print(f'Компании с прибылью выше среденей: {more_av}')
