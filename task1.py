"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""

import collections

firm = collections.namedtuple('firm', ['name', 'q1', 'q2', 'q3', 'q4', 'year_product', 'looser_flag'])

firm_number = int(input('Кол-во предприятий: '))

firms = []
for i in range(firm_number):
    name = input('Название предприятия: ')
    q1 = int(input('прибыль 1: '))
    q2 = int(input('прибыль 2: '))
    q3 = int(input('прибыль 3: '))
    q4 = int(input('прибиль 4: '))
    firms.append(firm(name, q1, q2, q3, q4, sum([q1, q2, q3, q4]), 'Unknown'))

mean_year_product = sum([_.year_product for _ in firms])/firm_number

loosers = []
winners = []
mediums = []
for firm in firms:
    if firm.year_product < mean_year_product:
        firm = firm._replace(looser_flag=1)
        loosers.append(firm.name)
    elif firm.year_product > mean_year_product:
        firm = firm._replace(looser_flag=0)
        winners.append(firm.name)
    else:
        mediums.append(firm.name)

print(f'Прибыль выше общей среднегодовой прибыли: {", ".join(winners)}') if len(loosers) > 0 else None
print(f'Прибыль ниже общей среднегодовой прибыли: {", ".join(loosers)}') if len(winners) > 0 else None
print(f'Прибыль равна общей среднегодовой прибыли: {", ".join(mediums)}') if len(mediums) > 0 else None