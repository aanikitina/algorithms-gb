"""
Task 5:

В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
"""

import random

SIZE = 10
MAX_LIMIT = 50
MIN_LIMIT = -10

numbers = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

max_negative = MIN_LIMIT # Из соображений, что меньше нет, как только
for number in numbers:
    if max_negative < number < 0:
        max_negative = number

print(numbers)
if max_negative > 0:
    print('В массиве нет отрицательных элементов')
else:
    print(f'Максимальный отрицательный элемент: {max_negative}')