"""
С помощью функции заполнить матрицы случайными числами. Написать функцию, вычисляющую сумму двух матриц.
Вывести на экран две исходные матрицы и их сумму.
Написать функцию по сложению 2-х матриц.
"""

import random


def create_matrix(n, c):
    matrix = []
    for i in range(0, n):
        matrix.append([])
        for j in range(0, n):
            matrix[i].append(random.randint(0, c))
    return matrix


def sum_el_matrix(matrix):
    s = 0
    for i in matrix:
        for j in i:
            s += j
    return s


def sum_matrix():
    pass


def show_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end='\t')
        print()

    print()


my_matrix1 = create_matrix(3, 1)
my_matrix2 = create_matrix(20, 20)

show_matrix(my_matrix1)
print(f'Sum matrix my_matrix1 - {sum_el_matrix(my_matrix1)} \n')
show_matrix(my_matrix2)
print(f'Sum matrix my_matrix2 - {sum_el_matrix(my_matrix2)} \n')

# for i in my_matrix1:
#     for j in i:
#         print(j, end='\t')
#     print()
#
# print()
