"""
Task 9:

Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.

"""

def get_sum_of_digits(number):
    s = 0

    while number // 10 != 0:
        s += number % 10
        number = number // 10

    s += number

    return s


final_n = 0
max_sum_of_d = 0

while True:
    a = int(input('Введите число:'))

    if a == 0:
        print(f'Искомое число с максимальной суммой цифр: {final_n}, сумма цифр: {max_sum_of_d}')
        break
    else:
        if get_sum_of_digits(a) > max_sum_of_d:
            final_n = a
            max_sum_of_d = get_sum_of_digits(a)

       # print(f'final_n = {final_n}, max_sum = {max_sum_of_d}')
