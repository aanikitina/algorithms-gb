"""
Task 1:

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

"""

import random

MIN_LIMIT = -100
MAX_LIMIT = 100
SIZE = 10


def bubble_sorting(array):
    n = 1
    while n < len(array):

        action = False
        for i in range(len(array) - n):

            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                action = True

        if action == False:
            print(f'sorted - {n - 1} iterations')
            break

        n += 1


numbers = [random.randint(MIN_LIMIT, MAX_LIMIT - 1) for _ in range(SIZE)]
print(f'Original array: {numbers}')

bubble_sorting(numbers)

print(f'Sorted array: {numbers}')