# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Python 3.6.5 x64

# 2/3

import sys
import random  # Переместил их сюда, а то как-то это не по PEP-8
import math


def show_size(x):  # Взял из урока, чуть изменил.
    # print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    byte_size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                byte_size += show_size(key)
                byte_size += show_size(value)
        elif not isinstance(x, str):
            for item in x:
                byte_size += show_size(item)
    return byte_size


memory_used = 0
iter_counter_n = set()
iter_counter_max_ = set()
iter_counter_min_ = set()
iter_counter_max_index = set()
iter_counter_min_index = set()
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
# и максимальный элементы в сумму не включать.

# import random
# import math

list_1 = [(random.randint(0, 100)) for _ in range(0, 10)]
memory_used += show_size(list_1)

min_ = math.inf
iter_counter_min_.add(min_)
max_ = -math.inf
iter_counter_max_.add(max_)
index = 0
summ_ = 0

for n in list_1:
    if n < min_:
        min_ = n
        iter_counter_min_.add(min_)  # сбор уникальных значений для вычисления максимального
        min_index = index
        iter_counter_min_index.add(min_index)  # сбор уникальных значений для вычисления максимального
    if n > max_:
        max_ = n
        iter_counter_max_.add(max_)  # сбор уникальных значений для вычисления максимального
        max_index = index
        iter_counter_max_index.add(max_index)  # сбор уникальных значений для вычисления максимального
    index += 1
    iter_counter_n.add(n)  # сбор  значений для вычисления максимального

memory_used += show_size(max(iter_counter_n))   # Вычисление
iter_counter_n = set()                          # и очистка для повторного использования

print(f'Исходный список:\n{list_1}\nмасимальное число {max_}, индекс {max_index}, минимальное число {min_}, индекс '
      f'{min_index}')

if min_index < max_index:
    print(f'промежуток между мин и макс значениями {list_1[min_index + 1:max_index]}')
    for n in list_1[min_index + 1:max_index]:
        summ_ += n
        iter_counter_n.add(n)  # и тут я задумался. А ведь прошлая n уже пуста? Стоит ли считать их вместе?
        # Предполагаю, что на всякий случай стоит.
else:
    print(f'промежуток между мин и макс значениями {list_1[max_index + 1:min_index]}')
    for n in list_1[max_index + 1:min_index]:
        summ_ += n
        iter_counter_n.add(n)
print(f'Сумма равна {summ_}')

if len(iter_counter_n) > 0:
    memory_used += show_size(max(iter_counter_n))  # Вычисление
memory_used += show_size(index)
memory_used += show_size(summ_)
memory_used += show_size(max(iter_counter_min_))
memory_used += show_size(max(iter_counter_max_))
memory_used += show_size(max(iter_counter_min_index))
memory_used += show_size(max(iter_counter_max_index))

print(f'было использовано {memory_used} байт памяти')
