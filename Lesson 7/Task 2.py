# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
# [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge(a, b):
    result = []
    while True:
        if len(a) > 0 and len(b) > 0:
            if a[0] < b[0]:
                result.append(a[0])
                a.pop(0)
            else:
                result.append(b[0])
                b.pop(0)
        elif len(a) > 0:
            result += a
            break
        elif len(b) > 0:
            result += b
            break
    return result


def merge_sort(list_):
    result = []
    for n in list_:
        result.append([n])
    while len(result) > 1:
        for i in (range(len(result) // 2)):
            result[i] = merge(result.pop(i), result[i])
    return result[0]


list_1 = [random.uniform(0.00, 49.99) for n in range(11)]  # округлил до двух знаков, 50 у нас исключается.

print(f'исходный список: \n{list_1}\nотсортированный список:\n{merge_sort(list_1)}')

# list_1.sort()
# print(f'для проверки\n{list_1}')
