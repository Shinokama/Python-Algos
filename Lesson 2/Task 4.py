# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с
# клавиатуры.

n = int(input('Введите количество элементов последовательности: '))

num = 1
i = int(-2)
res = 0
while n > 0:
    n = n - 1
    res = res + num
    num = num / i
print(f'Сумма {n} элементов последовательности: {res}')