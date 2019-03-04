"""
Task 2:
Сравнение алгоримтов нахождения простых чисел меньших n.

Замеры модулем cProfile показывают, что при увеличении n разрыв в скорости работы функций нелинейно растает.
Если на n = 5000 наблюдается разница в сотни (~700, из-за округления судить сложно) раз,
при n = 50000 функция "с решетом" корректно отрабатывает за 0.027 сек, а вторая функция уже не выдает результат
(за то время, которое мне было интересно ждать).

По результатам замера времени с помощью модуля timeit на маленьких n:
sieve_func демонстрирует зависимость t(n) близкую к линейной
simple_div очевидно имеет нелинейную зависимость t(n), что объясняет результат, (возможно O(n^2), тк вложенный цикл)
наблюдаемый на больших n модулем cProfile
"""

import cProfile


def sieve_func(n):

    sieve = [i for i in range(n)]

    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    return result


# cProfile.run('sieve_func(50000)')
#        1    0.000    0.000    0.000    0.000 task2.py:4(sieve_func)   - 50 функция работает слишком быстро для замера
#        1    0.001    0.001    0.001    0.001 task2.py:4(sieve_func)   - 5000
#        1    0.021    0.021    0.027    0.027 task2.py:11(sieve_func)  - 50000

"""
"task2.sieve_func(10)"
100 loops, best of 3: 2.48 usec per loop
"task2.sieve_func(15)"
100 loops, best of 3: 3.24 usec per loop
"task2.sieve_func(20)"
100 loops, best of 3: 4.16 usec per loop
"task2.sieve_func(25)"
100 loops, best of 3: 5.24 usec per loop
"task2.sieve_func(30)"
100 loops, best of 3: 6.1 usec per loop
"task2.sieve_func(50)"
100 loops, best of 3: 10.2 usec per loop

"""


def simple_div(n):

    numbers = [i for i in range(2, n)]

    for i, number in enumerate(numbers):
        for j in range(2, number):
            if number % j == 0:
                numbers[i] = 0

    result = [i for i in numbers if i != 0]
    return result


# cProfile.run('simple_div(50000)')
#        1    0.000    0.000    0.000    0.000 task2.py:41(simple_div)  - 50
#        1    0.734    0.734    0.735    0.735 task2.py:41(simple_div)  - 5000 хорошо видно, что функция отрабатывает в
#                                                                       сотни раз медленнее, чем реализация через решето
#       для n = 50000 дожидаться результата выполнения функции уже не хочется

"""
"task2.simple_div(10)"
100 loops, best of 3: 4.64 usec per loop
"task2.simple_div(15)"
100 loops, best of 3: 9.73 usec per loop
"task2.simple_div(20)"
100 loops, best of 3: 13.2 usec per loop
"task2.simple_div(25)"
100 loops, best of 3: 19.3 usec per loop
"task2.simple_div(30)"
100 loops, best of 3: 26.3 usec per loop
"task2.simple_div(50)"
100 loops, best of 3: 65.8 usec per loop

"""


# функции проверяем с n = 2. n - не включительно, ищем натуральные числа ДО n
def test_func():
    for i in range(2, 50):
        assert simple_div(i) == sieve_func(i)
        print(f'{i} test step OK')


#print(sieve_func(50))
#print(simple_div(50))



