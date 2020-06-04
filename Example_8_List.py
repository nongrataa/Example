"""Вы принимаете от пользователя последовательность чисел,
разделённых запятой. Составьте список и кортеж с этими числами."""
a = str(input('Введите числа - '))
my_list = a.split(',')
my_tuple = tuple(my_list)
print('List - ', my_list)
print('Tuple - ', my_tuple)
