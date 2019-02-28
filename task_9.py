"""
Task 9:

Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

SIZE_X, SIZE_Y = 4, 3
MAX_LIMIT = 10
MIN_LIMIT = -10

matrix = [[random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE_X)] for _ in range(SIZE_Y)]
for line in matrix:
    print(line)

min_line = matrix[0][:]

for line in matrix[1:]:
    for i, item in enumerate(line):
        if item < min_line[i]:
            min_line[i] = item


max_min = min_line[0]
for item in min_line:
    if item > max_min:
        max_min = item

print(f'Минимальные значения столбцов - {min_line}')
print(f'Максимальное из них = {max_min}')

