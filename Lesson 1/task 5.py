# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
chr1 = input('Введите строчную букву латинского алфавита (a - z) chr1 = ')
chr2 = input('Введите строчную букву латинского алфавита (a - z) chr2 = ')

chroffset = 96
chrnum1 = ord(chr1) - chroffset
chrnum2 = ord(chr2) - chroffset

if chrnum1 < chrnum2:
    chrdiff = chrnum2 - chrnum1 - 1
else:
    chrdiff = chrnum1 - chrnum2 - 1

print(f'номер первой буквы {chrnum1}')
print(f'номер второй буквы {chrnum2}')
print(f'Количество букв между буквами {chrdiff}')
