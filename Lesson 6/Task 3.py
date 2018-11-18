# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Python 3.6.5 x64

# 2/3

import sys
import random


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
iter_counter_max_count = set()
iter_counter_max_count_num = set()

# Определить, какое число в массиве встречается чаще всего.

#import random

list_1 = [(random.randint(0, 10)) for _ in range(0, 20)]


max_count = 0
max_count_num = 0

for n in list_1:
    if list_1.count(n) > max_count:
        max_count_num = n
        iter_counter_max_count.add(max_count_num)
        max_count = list_1.count(n)
        iter_counter_max_count_num.add(max_count)
    iter_counter_n.add(n)

print(f'Исходный список:\n{list_1}')
print(f'Наиболее часто встречающееся число: {max_count_num}\nВстречается {max_count} раз')

memory_used += show_size(list_1)
memory_used += show_size(max(iter_counter_n))
memory_used += show_size(max(iter_counter_max_count))
memory_used += show_size(max(iter_counter_max_count_num))
print(f'было использовано {memory_used} байт памяти')
