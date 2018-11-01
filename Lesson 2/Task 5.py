# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

STARTSYM = 32
ENDSYM = 127
table = ''
counter = 0
for n in range(STARTSYM, ENDSYM+1):
    counter = counter + 1
    if counter == 10:
        counter = 1
        table = f'{table}\n|{n: 3d} = {chr(n)}'
    else:
        table = f'{table}|{n: 3d} = {chr(n)}'

print(table)
