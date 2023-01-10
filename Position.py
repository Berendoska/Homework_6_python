
from random import randint
# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

first_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
second_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
third_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
four_list =  ["123", "234", 123, "567"]
five_list = []


def find_position_el(list_el, el) -> int:
    '''Функция сначала создает кортеж, в котором указаны индексы и их значения,и если под указанным индексом
    стоит искомое значние, ее идекс выводится в новый список. Далее функция выводит индекс второго вхождение искомого значения '''
    
    x = [i for i, pos in enumerate(list_el) if pos == el]
    if len(x)>1:
        result = x[1]
    else: 
        result = -1
    return result

        

print(find_position_el(first_list, "qwe"))
print(find_position_el(second_list, "йцу"))
print(find_position_el(third_list, "йцу"))
print(find_position_el(four_list, "123"))
print(find_position_el(five_list, "123"))

# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
first_list = [5, 6, 8, 9]
second_list = [5, 6, 8, 9, 5, 6]

def product_pair(a_list)-> list:

    ''' Функция создает зеркальный список и перемножает его с входящим списоком по парам. Функция работает для списоков
    с четным количеством элементов'''
    new_list = a_list[::-1]
    product = [a_list[i]*new_list[i] for i in range (len(a_list))]
    return product[:len(product)//2]

print(product_pair(first_list))
print(product_pair(second_list))

# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.


site_list = ['http://website.com',
'https://example.com',
'www.example.com',
'https://vk.com',
'http://www.geek.com',
'https://google.com'
]

domens = []

for i in range(len(site_list)):
    another_version = site_list[i].partition('//')[-1]
    another_version = another_version.partition('/')[0]
    domens.append(another_version)

print(domens, sep ='\n')


# 5 - Есть список случайных чисел в промежутке от 1 до 100, 
# количеством 200. Создайте список кортежей, 
# первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]
# Из списка  оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]



def create_tuple_divided_by_5() -> tuple:
    '''функция сначала создает кортеж из случайных чисел с индексами, далее создается два списка с индексами
    и значениями, которые добавляются в списки при условии, что номер с индексом не совпадает и в сумме они деляться на
    5. В итоге создаем кортеж, объеденяя эти два списка с помощью zip '''
    list_for_tuple = [randint(1,15) for i in range(1,15)]
    result = list(enumerate(list_for_tuple))
    print(*result)
    tul_new = []
    tul_new2 = []
    for index, number in result:
        if index!=number:
            if(index + number)%5 ==0:
                tul_new.append(index)
                tul_new2.append(number)
    new_tulip = list(zip(tul_new,tul_new2))
    return new_tulip

print(create_tuple_divided_by_5())









