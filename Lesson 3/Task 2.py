# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3,
# 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 – если индексация начинается с
# нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

list_1 = [(random.randint(0, 100)) for _ in range(0, 20)]
list_2 = list()
index = 0

for n in list_1:
    if n % 2 == 0:
        list_2.append(index)
    index += 1

print(f'Список чисел:\n{list_1}\nСписок индексов четных чисел\n{list_2}')
