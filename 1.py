# Вариант 4
# Найдите произведение элементов списка с нечетными номерами.
# Найдите наибольший элемент списка, затем удалите его и выведите новый

print('Вариант 4:')
from random import randint as ri
index_of_max, p, l = 0, 1, [ri(-99, 99) for i in range(ri(5, 20))]
print(l)
for i in range(len(l)):
    if l[i] % 2 != 0:
        p *= l[i]
    if l[i] > l[index_of_max]:
        index_of_max = i
print('Произведение нечётных:', p)
print('Наибольший элемент списка:', index_of_max, 'индекс')
l.pop(index_of_max)
print('Новый список:', '\n', l, '\n')


# Вариант 5
# Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
# Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.

print('Вариант 5:')
lst = [71, -98, 36, 2, -36, 0, 56, 0, -8]
min_number = 0
print(lst)
for j in range(len(lst)):
    if min_number > lst[j]:
        min_number = lst[j]
    if lst[j] == 0:
        del lst[j]
        lst.insert(0, 0)
if min_number % 2 == 0:
    print('Наименьший четный элемент списка:', min_number)
else:
    print('Первый элемент:', lst[0])
print('Новый список:', '\n', lst)