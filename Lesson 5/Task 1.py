# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

company = namedtuple('company', 'Name q1 q2 q3 q4 total')
company_list = []
company_count = int(input('Введите количество компаний'))

for n in range(company_count):
    Name = input(f'Введите имя компании {n+1}')

    q1 = int(input(f'введите прибыль за первый квартал для {Name}'))
    q2 = int(input(f'введите прибыль за первый квартал для {Name}'))
    q3 = int(input(f'введите прибыль за первый квартал для {Name}'))
    q4 = int(input(f'введите прибыль за первый квартал для {Name}'))
    total = q1 + q2 + q3 + q4
    company_list.append(company(Name, q1, q2, q3, q4, total))

mid_profit = 0
for n in company_list:
    mid_profit += n.total
else:
    mid_profit = mid_profit / len(company_list)


lesser_list = []
greater_list = []
for n in company_list:
    if n.total < mid_profit:
        lesser_list.append(n.Name)
    else:
        greater_list.append(n.Name)

print(f'Средняя прибыль за год среди всех компаний {mid_profit}')
print(f'Компании, которые заработали меньше: \n {lesser_list}')
print(f'компании, которые заработали больше: \n {greater_list}')

