
# 2.	Симметричная матрица.
# Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.

from math import sqrt
a = int(input('Высота:'))
b = int(input('Ширина:'))
square = []
for i in range(a):
    square.append([])
    for j in range(b):
        square[i].append(0)
x = sqrt(2)
d = a * x == b * x
print('\n', 'Матрица:')
for y in range(a):
    print(square[y])
if d == True:
    print('\n', 'Квадратная матрица  симметричнa')
else:
    print('\n', 'Квадратная матрица не симметричнa')









