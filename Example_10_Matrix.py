"""
Написать программу поиска минимального и максимального элементов матрицы и их индексов.
"""

def max_el_matrix(matrix):
    max_el = matrix[0][0]
    for i in matrix:
        for j in i:
            if j > max_el:
                max_el = j

    return max_el


def min_el_matrix(matrix):
    min_el = matrix[0][0]
    for i in matrix:
        for j in i:
            if j < min_el:
                min_el = j
    return min_el


mymatrix = [
    [1, 20, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f'max_el - {max_el_matrix(mymatrix)}')
print(f'min_el - {min_el_matrix(mymatrix)}')
print()

for i in mymatrix:
    for j in i:
        print(j, end="\t")
    print("")
