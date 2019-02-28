"""
Task 7:

В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random

SIZE = 10
MAX_LIMIT = 10
MIN_LIMIT = 0

numbers = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

# Для себя в определим, что min1 < min2
min1 = numbers[0]
min2 = numbers[0] + 1  # 1 - запас на случай, минимального первого элемента

for number in numbers[1:]: # 0 не проверяем, иначе в случае минимального 1 элемента min2 тоже будет перезаписан на знaчение min1
    if number < min1:
        min1, min2 = number, min1
    elif number < min2:
        min2 = number

print(f'Минимальный элемент: {min1}, второй минимальный: {min2}')