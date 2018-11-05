# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

list_1 = [n for n in range(2, 100)]
list_2 = [n for n in range(2, 10)]
for n in list_2:
    count = 0
    for m in list_1:
        count += 1 if m % n == 0 else 0
    print(f'Числу {n} кратны {count} чисел')
