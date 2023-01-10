import os
# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

os.system('cls')

def list_number_3():
    new_list = (list((-3)**i for i in range(int(input('Введите N: ')))))
    return new_list
print(list_number_3())