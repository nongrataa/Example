#Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

a = str(input('Введите строку - '))
if a == a[::-1]:
    print('Число полиндром')
else:
    print('Число не полиндром')