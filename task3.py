"""
Task 3:

Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках

"""

import random

MIN_LIMIT = -100
MAX_LIMIT = 100
M = 4
size = 2 * M + 1

numbers = [random.randint(MIN_LIMIT, MAX_LIMIT - 1) for _ in range(size)]
print(f'Original array: {numbers}')

max_array = []
# можно заменить len(numbers) на size, если ограничиться случаем генерации масиива заданной длины
for _ in range(len(numbers) // 2 + 1):
    max_i = max(numbers)
    max_array.append(max_i)
    numbers.remove(max_i)

print(f'median: {max_i}')
print(f'l_part: {max_array[:-1]}, r_part: {numbers}')