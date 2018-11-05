# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
# и максимальный элементы в сумму не включать.

import random
import math

list_1 = [(random.randint(0, 100)) for _ in range(0, 10)]
min_ = math.inf
max_ = -(math.inf)
index = 0
summ_ = 0

for n in list_1:
    if n < min_:
        min_ = n
        min_index = index
    if n > max_:
        max_ = n
        max_index = index
    index += 1

print(f'Исходный список:\n{list_1}\nмасимальное число {max_}, индекс {max_index}, минимальное число {min_}, индекс '
      f'{min_index}')

if min_index < max_index:
    print(f'промежуток между мин и макс значениями {list_1[min_index + 1:max_index]}')
    for n in list_1[min_index + 1:max_index]:
        summ_ += n
else:
    print(f'промежуток между мин и макс значениями {list_1[max_index + 1:min_index]}')
    for n in list_1[max_index + 1:min_index]:
        summ_ += n

print(f'Сумма равна {summ_}')