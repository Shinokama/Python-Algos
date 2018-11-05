# Определить, какое число в массиве встречается чаще всего.

import random

list_1 = [(random.randint(0, 10)) for _ in range(0, 20)]
max_count = 0
max_count_num = 0

for n in list_1:
    if list_1.count(n) > max_count:
        max_count_num = n
        max_count = list_1.count(n)

print(f'Исходный список:\n{list_1}')
print(f'Наиболее часто встречающееся число: {max_count_num}\nВстречается {max_count} раз')