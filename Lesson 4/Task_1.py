# Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего задания первых
# трех уроков.


# Алгоритм 1

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.


def test1(num):

    list_1 = [n for n in range(2, num)]
    list_2 = [n for n in range(2, 10)]
    for n in list_2:
        count = 0
        for m in list_1:
            count += 1 if m % n == 0 else 0
        return f'Числу {n} кратны {count} чисел'

# timeit -n 100 -s "import Task_1" "Task_1.test1(10)"
# 100 loops, best of 5: 2.57 usec per loop
#timeit -n 100 -s "import Task_1" "Task_1.test1(100)"
#100 loops, best of 5: 11.5 usec per loop
# timeit -n 100 -s "import Task_1" "Task_1.test1(1000)"
# 100 loops, best of 5: 161 usec per loop
# timeit -n 100 -s "import Task_1" "Task_1.test1(10000)"
# 100 loops, best of 5: 2.01 msec per loop
# timeit -n 100 -s "import Task_1" "Task_1.test1(100000)"
# 100 loops, best of 5: 19.5 msec per loop
# Похоже, сложность линейная. На порядок больше данные -> на порядок больше время.

# Алгоритм 2

# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3,
# 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 – если индексация начинается с
# нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

def test2(n):
    list_1 = [(random.randint(0, 100)) for _ in range(0, n)]
    list_2 = list()
    index = 0

    for n in list_1:
        if n % 2 == 0:
            list_2.append(index)
        index += 1

    return f'Список чисел:\n{list_1}\nСписок индексов четных чисел\n{list_2}'

# timeit -n 100 -s "import Task_1" "Task_1.test2(10)"
# 100 loops, best of 5: 16.1 usec per loop
#
# timeit -n 100 -s "import Task_1" "Task_1.test2(100)"
# 100 loops, best of 5: 182 usec per loop
#
# timeit -n 100 -s "import Task_1" "Task_1.test2(1000)"
# 100 loops, best of 5: 2.02 msec per loop
#
# timeit -n 100 -s "import Task_1" "Task_1.test2(10000)"
# 100 loops, best of 5: 20.1 msec per loop
#
# timeit -n 100 -s "import Task_1" "Task_1.test2(100000)"
# 100 loops, best of 5: 205 msec per loop

# Зависимость так же линейная

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
# и максимальный элементы в сумму не включать.

import math


def test3(num):
    list_1 = [(random.randint(0, 100)) for _ in range(0, num)]
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

    # print(f'Исходный список:\n{list_1}\nмасимальное число {max_}, индекс {max_index}, минимальное число {min_}, индекс '
    #      f'{min_index}')

    if min_index < max_index:
        # print(f'промежуток между мин и макс значениями {list_1[min_index + 1:max_index]}')
        for n in list_1[min_index + 1:max_index]:
            summ_ += n
    else:
        # print(f'промежуток между мин и макс значениями {list_1[max_index + 1:min_index]}')
        for n in list_1[max_index + 1:min_index]:
            summ_ += n

    return f'Сумма равна {summ_}'

# timeit -n 100 -s "import Task_1" "Task_1.test3(10)"
# 100 loops, best of 5: 14.8 usec per loop
#
# timeit -n 100 -s "import Task_1" "Task_1.test3(100)"
# 100 loops, best of 5: 189 usec per loop
#
# timeit -n 100 -s "import Task_1" "Task_1.test3(1000)"
# 100 loops, best of 5: 1.88 msec per loop
#
# timeit -n 100 -s "import Task_1" "Task_1.test3(10000)"
# 100 loops, best of 5: 19.1 msec per loop
#
# timeit -n 100 -s "import Task_1" "Task_1.test3(100000)"
# 100 loops, best of 5: 188 msec per loop
#
# И опять линейная зависимость.
