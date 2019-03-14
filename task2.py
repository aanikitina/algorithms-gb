"""
Task 2:

Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.

"""

import random
from collections import deque

MIN_LIMIT = 0
MAX_LIMIT = 50
SIZE = 10


def merge_sort(array):

    if len(array) < 2:
        return array

    left = deque(merge_sort(array[:len(array) // 2]))
    right = deque(merge_sort(array[len(array) // 2:]))

    merged = []

    while len(left) > 0 or len(right) > 0:

        if not (len(left) > 0):
            merged.append(right.popleft())
        elif not (len(right) > 0):
            merged.append(left.popleft())

        elif left[0] < right[0]:
                merged.append(left.popleft())
        else:
            merged.append(right.popleft())

        # print(merged)

    return merged


numbers = [random.uniform(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(f'Original array: ')
print(',\t'.join([f'{i:.3f}' for i in numbers]))

numbers = merge_sort(numbers)
print(f'Sorted array: ')
print(',\t'.join([f'{i:.3f}' for i in numbers]))