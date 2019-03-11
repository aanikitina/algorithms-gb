import sys
from collections import namedtuple
import platform

def get_size_func(x, storage, level=0, parent=None):

        # if parent == None:
        #     print('\t' * level, f'id = {id(x)}, type = {type(x)}, size = {sys.getsizeof(x)}, obj = {x}')
        # else:
        #     print('\t' * level, f'id = {id(x)}, type = {type(x)}, size = {sys.getsizeof(x)}, obj = {x}, parent = {parent[0]}, {parent[1]}')
        storage.append(variable(id(x), type(x), sys.getsizeof(x), parent))

        if hasattr(x, '__iter__'):
            parent = (id(x), type(x),)
            if hasattr(x, 'items'):
                for key, value in x.items():
                    get_size_func(key, storage, level + 1, parent)
                    get_size_func(value, storage, level + 1, parent)
            elif not isinstance(x, str):
                for item in x:
                    get_size_func(item, storage, level + 1, parent)

def get_size_multiple(x_list, storage):
    for x in x_list:
        get_size_func(x, storage, level=0, parent=None)


variable = namedtuple('variable', ['id', 'type', 'size', 'parent'])
storage = []


def get_storage_info(storage):

    new_storage = []
    new_storage_size, storage_size = 0, 0
    for item in storage:
        storage_size += item.size
        if item.id not in [_[0] for _ in new_storage]:
            # print(item)
            new_storage.append((item.id, item.size))
            new_storage_size += item.size
    print(f'Sum of sizes in storage: {storage_size}')
    print(f'There are {len(storage)} items in storage, {len(new_storage)} unique items. Size of unique = {new_storage_size}.')


"""
Task 2:

Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во
второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""


import random

SIZE = 10
N_MAX_LIMIT = 10000
N_MIN_LIMIT = 0


def implementation1(storage):

    numbers = [random.randint(N_MIN_LIMIT, N_MAX_LIMIT) for _ in range(SIZE)]

    odds = []
    evens = []

    for i in range(SIZE):
        if (numbers[i] % 2) == 0:
            odds.append(i)
        else:
            evens.append(i)

    get_size_multiple([numbers, odds, evens, i], storage)

    print(numbers)
    print(f'Odd number ids: {odds}')
    print(f'Even number ids: {evens}')



def implementation2(storage):

    numbers = tuple([random.randint(N_MIN_LIMIT, N_MAX_LIMIT) for _ in range(SIZE)])

    odds = []
    evens = []

    for i in range(SIZE):
        if (numbers[i] % 2) == 0:
            odds.append(i)
        else:
            evens.append(i)

    get_size_multiple([numbers, odds, evens, i], storage)

    print(numbers)
    print(f'Odd number ids: {odds}')
    print(f'Even number ids: {evens}')


def implementation3(storage):

    numbers = tuple([random.randint(N_MIN_LIMIT, N_MAX_LIMIT) for _ in range(SIZE)])

    odds = ()
    evens = ()

    for i in range(SIZE):
        if (numbers[i] % 2) == 0:
            odds = odds + (i,)
        else:
            evens = evens + (i,)

    get_size_multiple([numbers, odds, evens, i], storage)

    print(numbers)
    print(f'Odd number ids: {odds}')
    print(f'Even number ids: {evens}')



print(f'System: {platform.platform()}')
print(f'Python version: {platform.python_version()}')

print('Implementation1:') # массивы
random.seed(123456)
storage = []
get_size_multiple([SIZE, N_MAX_LIMIT, N_MIN_LIMIT], storage)
implementation1(storage)
get_storage_info(storage)


print('Implementation2:') # вместо исходного массива создается кортеж
random.seed(123456)
storage = []
get_size_multiple([SIZE, N_MAX_LIMIT, N_MIN_LIMIT], storage)
implementation2(storage)
get_storage_info(storage)


print('Implementation3:') # вместо всех массивов используются кортежи
random.seed(123456)
storage = []
get_size_multiple([SIZE, N_MAX_LIMIT, N_MIN_LIMIT], storage)
implementation3(storage)
get_storage_info(storage)


"""
Так как в Python заранее создает и хранит небольшие целые числа и другие часто используемые объекты 
для "честного" подсчета используемой памяти недостаточно написать функцию, рекурсивно проходяющую по сложным объектам и
возвращающую размеры вложенных объектов. Сложные объекты могут содержать в себе повторяющиеся объекты и включать объекты, 
"создаваемые" по умолчанию (None, небольшие int и тд). Для того, чтобы избежать учета памяти, затрачиваемой на объект,
на который ссылаются множество переменных, в функции get_storage_info(storage) происходит учет уникальных объектов 
в памяти, где под уникальностью подразумевается уникальный id. В такой небольшой программе, возможно, разница учета не 
очень видна, но в общем случае, я думаю, правильнее считать так.

Каждому вызову различных имплементаций также должен предшествовать "сброс" random seed. Тк заполнение исходного массива 
также влияет на затрачиваемую память.

Вывод: использование кортежей вместо простых массивов позволяет экономить память, однако работать в этой программе
скорее всего будет медленнее, тк при добавлении элемента к кортежу, создается новый кортеж из-за отсутсвия 
резервирования дополнительной памяти (это и позводяет экономить память, но не скорость).

"""


#
#  MacBook-Pro-Anastasia:algorithms anastasia$ python task1.py
# System: Darwin-18.2.0-x86_64-i386-64bit
# Python version: 3.6.8


# Implementation1:
# [4745, 482, 2861, 36, 1262, 835, 4399, 465, 1907, 3752]
# Odd number ids: [1, 3, 4, 9]
# Even number ids: [0, 2, 5, 6, 7, 8]

# Sum of sizes in storage: 1080
# There are 27 items in storage, 25 unique items. Size of unique = 1028.


# Implementation2:
# (4745, 482, 2861, 36, 1262, 835, 4399, 465, 1907, 3752)
# Odd number ids: [1, 3, 4, 9]
# Even number ids: [0, 2, 5, 6, 7, 8]

# Sum of sizes in storage: 1016
# There are 27 items in storage, 25 unique items. Size of unique = 964.


# Implementation3:
# (4745, 482, 2861, 36, 1262, 835, 4399, 465, 1907, 3752)
# Odd number ids: (1, 3, 4, 9)
# Even number ids: (0, 2, 5, 6, 7, 8)

# Sum of sizes in storage: 968
# There are 27 items in storage, 25 unique items. Size of unique = 916.

