"""
Составить программу, позволяющую с помощью датчика случайных чисел сформировать матрицу размерностью N.
Вывести элементы находящиеся ниже побочной диагонали.
Определить:
сумму элементов, лежащих ниже побочной диагонали;
минимальный элемент, лежащий ниже побочной диагонали;
произведение ненулевых элементов последней строки.
"""


def under_side_diagonal(matrix):
    a = len(matrix[1]) - 1
    under = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j > a:
                under.append(matrix[i][j])
        a -= 1
    return under


def sum_under_side_diagonal(matrix):
    sum = 0
    for i in matrix:
        sum += i
    return sum


def min_el_under_side_diagonal(matrix):
    min_el = matrix[0]
    for i in matrix:
        if i < min_el:
            min_el = i
    return min_el


my_matrix = [
    [3, 5, 3, 5],
    [7, 3, 5, 6],
    [9, 6, 1, 3],
    [4, 2, 2, 9]
]

print(f'Under side diagonal - {under_side_diagonal(my_matrix)}')
print(f'Sum under side diagonal - {sum_under_side_diagonal(under_side_diagonal(my_matrix))}')

for i in my_matrix:
    for j in i:
        print(j, end='\t')
    print()
