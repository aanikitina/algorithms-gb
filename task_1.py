"""
Task 1:
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

x = int(input('Введите целое трехзначное число: '))

s = x % 10
p = x % 10

x = x // 10

s = s + x%10
p = p * x%10

x = x // 10

s = s + x
p = p * x

print(f'Произведение цифр = {p}; Сумма цифр = {s}')