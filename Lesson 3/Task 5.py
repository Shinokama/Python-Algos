# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random
import math

list_1 = [(random.randint(-10, 10)) for _ in range(0, 20)]
index = 0
max = -(math.inf)
max_index = 0

for n in list_1:
    if 0 > n > max:
        max = n
        max_index = index
    index += 1

print(f'Исходный список:\n{list_1}')
if max == -(math.inf):
    print(f'В этот раз отрицательные числа не были сгенерированы.')
else:
    print(f'Максимельное отрицательное значение: {max}, его индекс: {max_index}')
