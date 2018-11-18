# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа.

from collections import deque


def hex_to_num(hex_number):
    result = deque()
    for n in range(len(hex_number)):
        result.append(hex_to_num_dict[hex_number[n]])
    return result


def num_to_hex(hex_number):
    result = deque()
    for n in range(len(hex_number)):
        result.append(num_to_hex_dict[hex_number[n]])
    return result


def summ_hex_numbers(hex_number_1, hex_number_2):
    hex_number_1.reverse()
    hex_number_2.reverse()
    result = deque([])
    # определение максимального количества симовлов
    hex_max_len = len(hex_number_1) if len(hex_number_1) >= len(hex_number_2) else len(hex_number_2)

    while len(hex_number_1) < hex_max_len:  # доведение до одинакового количества символов
        hex_number_1.append(0)
    while len(hex_number_2) < hex_max_len:
        hex_number_2.append(0)
    while len(result) < hex_max_len:
        result.append(0)

    for n in range(hex_max_len):
        result[n] = hex_number_1[n] + hex_number_2[n]
    result.reverse()
    hex_number_1.reverse()
    hex_number_2.reverse()
    return prepare_hex(result)


def multiple_hex_numbers(hex_number_1, hex_number_2):
    hex_number_1.reverse()
    hex_number_2.reverse()
    result = deque([0])

    summ_list = []

    for n in range(len(hex_number_1)):
        semi_result = deque()
        for m in range(len(hex_number_2)):
            semi_result.append(hex_number_1[n] * hex_number_2[m])
        for o in range(n):
            semi_result.appendleft(0)
        semi_result.reverse()
        summ_list.append(prepare_hex(semi_result))

    for n in summ_list:
        result = summ_hex_numbers(result, n)
    return prepare_hex(result)


def prepare_hex(hex_number):
    hex_number.reverse()
    for n in range(len(hex_number)):
        if hex_number[n] // 16 >= 1:
            if n+1 < len(hex_number):
                hex_number[n + 1] += hex_number[n] // 16
            else:
                hex_number.append(hex_number[n] // 16)
            hex_number[n] = hex_number[n] % 16
    hex_number.reverse()
    return hex_number


hex_to_num_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                   'C': 12,'D': 13, 'E': 14, 'F': 15}

num_to_hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                   12: 'C', 13: 'D', 14: 'E', 15: 'F'}


source_num_1 = deque(input('Введите первое число\n'))
source_num_2 = deque(input('Введите второе число\n'))

# тестовые значения

# source_num_1 = deque('AA65')
# source_num_2 = deque('B2C3')


# Преобразование данных для работы
num_1 = hex_to_num(source_num_1)
num_2 = hex_to_num(source_num_2)

print('Пользовтель веел числа', ''.join(source_num_1) + ' ' + ''.join(source_num_2))  # не нашел способа применить f
# строку с тем же эффектом
print(f'Числа сохранены как {list(source_num_1)} и {list(source_num_2)}')
print(f'Сумма чисел равна {num_to_hex(summ_hex_numbers(num_1, num_2))}')
print(f'Произведение числео равно {num_to_hex(multiple_hex_numbers(num_1, num_2))}')