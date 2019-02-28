"""
Task 1:

В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
"""
import random

N_MAX_LIMIT = 99
N_MIN_LIMIT = 2
D_MAX_LIMIT = 9
D_MIN_LIMIT = 2


numbers = [i for i in range(N_MIN_LIMIT, N_MAX_LIMIT + 1)]
divider = random.randint(D_MIN_LIMIT, D_MAX_LIMIT + 1)
print(f'Divider - {divider}')

result_list = []

for number in numbers:
    if (number % divider) == 0:
        result_list.append(number)

print(len(result_list))