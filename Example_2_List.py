"""
a = [1, 1, 7, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 7, 10, 11, 13, 89].
Нужно вернуть список, который состоит из элементов, общих для этих двух списков."""

a = [1, 1, 7, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 7, 10, 11, 12, 13, 89]
c = []
for i in a:
    for j in b:
        if i == j and i not in c:
            c.append(i)

print(c)
