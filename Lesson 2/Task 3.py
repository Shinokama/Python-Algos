# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
# введено число 3486, то надо вывести число 6843.

# Вариант один
num = input('Введите натуральное число ')
i = 1
res = ''
while len(num) - i >= 0:
    res = res + num[len(num) - i]
    i = i + 1
else:
    print(f'{res}')


# Вариант 2 - он мне нравится больше, но я не придумал, как его нарисовать на блок схеме.


def reflect(number, offset):
    digit = len(number) - offset
    if digit == 0:
        return number[0]
    if digit > 0:
        return f'{number[digit]}{reflect(number, offset + 1)}'


num = input('Введите натуральное число ')

print(reflect(num, 1))
