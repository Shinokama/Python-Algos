# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

import random


def bubble_sort(x):
    border = len(x) - 1
    changed = True
    while border > 0 and changed:
        changed = False
        for i in range(border):
            if x[i] < x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                changed = True
        border -= 1
    return x


list_1 = [random.randint(-100, 99) for n in range(10)]
print(f'исходный список: \n{list_1}\nотсортированный список:\n{bubble_sort(list_1)}')
