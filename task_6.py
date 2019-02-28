"""
Task 6:

В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

# так и не уверена, считается ли такая функция читерской в домашке)) пусть декан разберется
def interval_sum(a_id, b_id, array):
    array_sum = 0
    for item in array[a_id + 1 : b_id]:
        array_sum += item
    return array_sum


SIZE = 10
MAX_LIMIT = 100
MIN_LIMIT = 0

numbers = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

# Будет найден индекс первого встретившегося максимального/минимального элемента, если таких в массиве несколько
max_id = 0
min_id = 0
for i in range(1, SIZE):  # начинать с 0 элемента не нужно, тк это значение присвоено по умолчанию
    if numbers[i] > numbers[max_id]:
        max_id = i
    if numbers[i] < numbers[min_id]:
        min_id = i

print(f'Максимальный элемент: {numbers[max_id]}, минимальный: {numbers[min_id]}')

if min_id - max_id == abs(-1):
    print(f'Минимальный и максимальный элементы - соседние, Сумма = 0')
elif max_id > min_id:
    print(f'Сумма = {interval_sum(min_id, max_id, numbers)}')
else:
    print(f'Сумма = {interval_sum(max_id, min_id, numbers)}')