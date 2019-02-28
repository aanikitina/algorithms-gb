"""
Task3:

В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 10
MAX_LIMIT = 100
MIN_LIMIT = 0

numbers = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

max_id = 0
min_id = 0
for i in range(1, SIZE):
    if numbers[i] > numbers[max_id]:
        max_id = i
        print(f'new max {numbers[i]}, {max_id}')
    if numbers[i] < numbers[min_id]:
        min_id = i
        print(f'new min {numbers[i]}, {min_id}')

print(f'Original array: {numbers}')
numbers[min_id], numbers[max_id] = numbers[max_id], numbers[min_id]
print(f'Modified array: {numbers}')