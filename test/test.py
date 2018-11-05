a = [1, 2]
b = a
a.append(3)
b.append(3)
print(a)

c = [a] * 2
print(c[0])