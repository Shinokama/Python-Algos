# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше ее.

# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
# который не рассматривался на уроках.


import random


def median_find(list_):
    i = 0
    for n in list_:
        less_points = 0
        greater_points = 0
        equal_points = 0
        for m in range(len(list_)):
            if m != i:
                if n > list_[m]:
                    less_points += 1
                elif n < list_[m]:
                    greater_points += 1
                else:
                    equal_points += 1
        i += 1
        if abs(less_points - greater_points) == 0 or abs(less_points - greater_points) == equal_points:
            return n




m = 10
list_1 = [random.randint(-100, 99) for n in range(2*m + 1)]

print(f'Медианой массива\n{list_1}\nявляется число {median_find(list_1)}')

# list_1.sort()
# print(f'для проверки\n{list_1}\n число {list_1[(len(list_1) // 2)]}')


