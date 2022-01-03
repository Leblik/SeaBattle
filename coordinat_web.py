# Add axis for function 'print_fields'

# Печать элементов списка с новой строки, в столбик без цикла, через join
list_a = [1, 2, 3, 4, 5]
print('\n'.join([str(elem) for elem in list_a]))

# Перебираем элементы списка циклом for в столбик
y_axis = list(range(1, 11))
for elem in y_axis:
    print(" " * 7, elem, end="\n")

# Перебираем элементы списка циклом for в строчку
x_axis = list(range(1, 11))
print("\n", " " * 12, end='')
for elem in x_axis:
    print(elem, end=' ')
print('\n')

a = [str(i) for i in range(1, 11)]
for elem in a:
    print(elem, end=' ')
print('\n')

# Перебираем элементы списка распоковав их *
x_axis = range(1, 11)
print(*range(1, 11))
print(*x_axis)

a = [*range(1, 11)]
print(a)
