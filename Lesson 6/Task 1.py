# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Python 3.6.5 x64

# 1/3

import sys


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


# def show_size_max(x):  # для измерения занимаемого объема максимального из итерируемых элементов
#     byte_size = show_size(max(x))
#     return byte_size


memory_used = 0
iter_counter_n = set()
iter_counter_m = set()
iter_counter_count = set()

# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

list_1 = [n for n in range(2, 100)]
list_2 = [n for n in range(2, 10)]
for n in list_2:
    iter_counter_n.add(n)  # Сбор уникальных значений n
    count = 0
    for m in list_1:
        count += 1 if m % n == 0 else 0
        iter_counter_m.add(m)  # Сбор уникальных значений m
    iter_counter_count.add(count)  # Сбор уникальных максимальных значений count
    print(f'Числу {n} кратны {count} чисел')

memory_used += show_size(list_1)
memory_used += show_size(list_2)
# memory_used += show_size(count)  # тут хорошо бы измерить максимальное значение count, n и m а не последние. - Подумал
# я и запилил.
memory_used += show_size(max(iter_counter_n))
memory_used += show_size(max(iter_counter_m))
memory_used += show_size(max(iter_counter_count))
print(f'было использовано {memory_used} байт памяти')
