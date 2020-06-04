# Отсортируйте словарь по значению в порядке возрастания и убывания.
def sort_dict(d, typ_sort='v'):
    """
    :param d: dict
    :type d: dict
    :param typ_sort: Typ sort
    :type typ_sort: str
    :return: int
    :type:int
    """
    list_key = list(d.keys())
    list_key.sort()

    if typ_sort == 'u':
        list_key.reverse()

    for i in list_key:
         print(f'{i} : {d[i]}')
    return


d = {'b': 2, 'c': 3, 'a': 1}
sort_dict(d, 'u')
