"""
Написать программу, выводящую на экран строку матрицы, сумма элементов которой максимальна.
"""

def max_str_matrix(matrix):
    a = 0
    max_str = []
    for i in matrix:
        sum = 0
        b = []
        for j in i:
            sum += j
            b.append(j)
        if sum > a:
            a = sum
            max_str = b
    return max_str


my_matrix = [
    [1, 3, 5, 4],
    [4, 3, 6, 1],
    [1, 3, 3, 5],
    [5, 2, 1, 3]
]

print(f'Максимальная строка в матрице - {max_str_matrix(my_matrix)}')
