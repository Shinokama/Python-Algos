# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
#  вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые
#  данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
#  Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
#  и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0
# в качестве делителя.

while True:
    operation = input('Введите знак операции (+, -, *, /), либо 0 для выхода \n')
    if operation == '0' or '+' or '-' or '*' or '/':
        if operation == '0':
            print('Выход из программы. До новых встреч!')
            break
        else:
            firstnum = int(input('Введите первое число: '))
            secondnum = int(input('Введите второе число: '))
            if operation == '+':
                result = firstnum + secondnum
            elif operation == '-':
                result = firstnum - secondnum
            elif operation == '*':
                result = firstnum * secondnum
            else:
                if secondnum == 0:
                    result = 'Невозможно использовать ноль в качестве делителя.\n'
                else:
                    result = firstnum * secondnum
            print(result)
    else:
        print('Неверный знак операции, попробуйте еще раз.')