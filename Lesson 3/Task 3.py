# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import math

list_1 = [(random.randint(0, 100)) for _ in range(0, 10)]
min_ = math.inf
max_ = -(math.inf)
index = 0

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
list_1[min_index] = max_
list_1[max_index] = min_
print(f'Измененный список:\n{list_1}')
