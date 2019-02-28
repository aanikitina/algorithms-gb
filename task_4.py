"""
Task 4:

Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 10
MAX_LIMIT = 3
MIN_LIMIT = 0

numbers = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
numbers_unique = list(set(numbers))

most_freq = numbers_unique[0]
max_freq = 0
for number in numbers_unique:
    freq = 0
    for i in numbers:
        if i == number:
            freq += 1
    if freq > max_freq:
        max_freq = freq
        most_freq = number
        print(f'new max freq {freq}, {number}')
print(f'Заданный массив: {numbers}')
print(f'Чаще всего встречается число {most_freq}. {max_freq} раз(а).')
