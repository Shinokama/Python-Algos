# Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

# Решето


def eratosphene(i):
    list_1 = []
    number = 1  # В последний раз число 1 относили к простым в 1899 году. Но, полагаю, так аутентичнее. Можно взять 2.
    while len(list_1) - list_1.count(0) < i:
        simple = True
        for n in list_1:
            if n > 1 and number % n == 0:
                simple = False
                break
        if simple:
            list_1.append(number)
        number += 1
    else:
        return list_1[-1]


# timeit -n 100 -s "import Task_2" "Task_2.eratosphene(10)"
# 100 loops, best of 5: 17.8 usec per loop
#
# timeit -n 100 -s "import Task_2" "Task_2.eratosphene(100)"
# 100 loops, best of 5: 3.02 msec per loop
#
# timeit -n 100 -s "import Task_2" "Task_2.eratosphene(1000)"
# 100 loops, best of 5: 399 msec per loop
# При увеличении на порядок номера простого числа, время выполнения возрастает на 2 порядка, полагаю, сложнос
# но это не точно.


# Не решето


def eratosphenone(i):
    number = 2  # первое простое число
    simple_count = 0
    last_simple = 2
    while simple_count < i:
        simple = True
        for n in range(2, number):  # не используя решето, приходится перебирать все числа.
            if number % n == 0:
                simple = False
                break
        if simple:
            last_simple = number
            simple_count += 1
        number += 1
    else:
        return last_simple

# timeit -n 100 -s "import Task_2" "Task_2.eratosphenone(10)"
# 1 loop, best of 5: 16 usec per loop
#
# timeit -n 100 -s "import Task_2" "Task_2.eratosphenone(100)"
# 1 loop, best of 5: 1.41 msec per loop
#
# timeit -n 100 -s "import Task_2" "Task_2.eratosphenone(1000)"
# 1 loop, best of 5: 281 msec per loop
#
# timeit -n 100 -s "import Task_2" "Task_2.eratosphenone(10000)"
# 1 loop, best of 5: 41.6 sec per loop
# Оставлять выполняться последний - было моей ошибкой, комп ушел в себя =)
# на лицо геометрическая прогрессия времени при увеличении номеря простого числа.