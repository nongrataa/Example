#Напишите программу для слияния нескольких словарей в один.
my_dict1 = {'1': 1, '2': 2, '3': 3}
my_dict2 = {'4': 4, '5': 5, '6': 6}
my_dict3 = {'7': 7, '8': 8, '9': 9}
print('my_dict1 - ', my_dict1)
print('my_dict2 - ', my_dict2)
print('my_dict3 - ', my_dict3)

for i in (my_dict1, my_dict2, my_dict3):
    my_dict1.update(i)

print(my_dict1)
