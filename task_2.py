"""
Task 2:

Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во
второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random

SIZE = 10
N_MAX_LIMIT = 100
N_MIN_LIMIT = 0

numbers = [random.randint(N_MIN_LIMIT, N_MAX_LIMIT) for _ in range(SIZE)]

odds = []
evens = []

for i in range(SIZE):
    if (numbers[i] % 2) == 0:
        odds.append(i)
    else: evens.append(i)

print(numbers)
print(f'Odd number ids: {odds}')
print(f'Even number ids: {evens}')