"""
Напишите программу, которая принимает имя файла и выводит его расширение.
Если расширение у файла определить невозможно, выбросите исключение.
"""
def type_file():
    while True:
        a = str(input('Введите название файла - '))

        if '.' in a:
            return print('Расширение файла - ', a.split('.')[-1])
            break
        else:
            print('Некорректное название файла, попробуйте ещё раз.')


type_file()