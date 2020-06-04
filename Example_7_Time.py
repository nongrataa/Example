"""Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды."""

a = int(input('Введите секунды - '))
if a <= 59:
    s = a % 60
    print(f'day - 0, hours - 0, minutes - 0, second - {s}')
elif a <= 3599 and a >= 60:
    m = a // 60
    s = a % 60
    print(f'day - 0, hours - 0, minutes - {m}, second - {s}')
elif a <= 86399 and a >= 3600:
    h = a // 3600
    m = (a % 3600) // 60
    s = a % 60
    print(f'day - 0, hours - {h}, minutes - {m}, second - {s}')
elif a >= 86400:
    d = a // 86400
    h = (a % 86400) // 3600
    m = (a % 3600) // 60
    s = a % 60
    print(f'day - {d}, hours - {h}, minutes - {m}, second - {s}')
