"""
Task 1:
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Реализации с рекурсией, циклом и циклом + стандартные функции нахождения max/min:
1) Нахождение суммы элементов множества от a_id до b_id с помощью цикла
2) Нахождение суммы элементов множества от a_id до b_id рекурсивно
3) Нахождение суммы элементов множества от a_id до b_id в цикле, + встроенные функции

Имеет смысл сравнить функции получения суммы элементов массива в интервале отдельно от нахождения max/min,
для этого были написаны "обертки":
test_interval_sum_loops(), test_interval_sum_rec()
и проанализированы с помощью cProfile

"""

import random
import cProfile

# Вспомогательная функция генерации массива
def get_array(size):

    random.seed(11111)

    SIZE = size
    MAX_LIMIT = 10000
    MIN_LIMIT = -10000

    numbers_array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
    return numbers_array



# 1) Нахождение суммы элементов множества от a_id до b_id с помощью цикла

def interval_sum_loops(a_id, b_id, array):
    array_sum = 0
    for item in array[a_id + 1 : b_id]:
        array_sum += item
    return array_sum


def main_with_loops(size):

    numbers = get_array(size)

    max_id = 0
    min_id = 0
    for i in range(1, size):
        if numbers[i] > numbers[max_id]:
            max_id = i
        if numbers[i] < numbers[min_id]:
            min_id = i

    if abs(min_id - max_id) == 1:
        return 0
    elif max_id > min_id:
        return interval_sum_loops(min_id, max_id, numbers)
    else:
        return interval_sum_loops(max_id, min_id, numbers)


# cProfile.run('main_with_loops(10)')
#         1    0.000    0.000    0.000    0.000 task1.py:13(get_array)
#         1    0.000    0.000    0.000    0.000 task1.py:27(interval_sum_loops)
#         1    0.000    0.000    0.000    0.000 task1.py:33(main_with_loops)
#
# cProfile.run('main_with_loops(1000)')
#         1    0.000    0.000    0.002    0.002 task1.py:13(get_array)
#         1    0.000    0.000    0.000    0.000 task1.py:27(interval_sum_loops)
#         1    0.000    0.000    0.002    0.002 task1.py:33(main_with_loops)
#
# cProfile.run('main_with_loops(10000)')
#         1    0.000    0.000    0.023    0.023 task1.py:13(get_array)
#         1    0.000    0.000    0.000    0.000 task1.py:27(interval_sum_loops)
#         1    0.001    0.001    0.024    0.024 task1.py:33(main_with_loops)
#
# cProfile.run('main_with_loops(100000)')
#         1    0.000    0.000    0.206    0.206 task1.py:13(get_array)
#         1    0.001    0.001    0.001    0.001 task1.py:27(interval_sum_loops)
#         1    0.014    0.014    0.220    0.220 task1.py:33(main_with_loops)
#
# cProfile.run('main_with_loops(500000)')
#         1    0.000    0.000    1.031    1.031 task1.py:13(get_array)
#         1    0.006    0.006    0.006    0.006 task1.py:27(interval_sum_loops)
#         1    0.067    0.067    1.104    1.104 task1.py:33(main_with_loops)


# "task1.main_with_loops(10)"
# 100 loops, best of 3: 19.7 usec per loop
#  "task1.main_with_loops(100)"
# 100 loops, best of 3: 120 usec per loop
# "task1.main_with_loops(1000)"
# 100 loops, best of 3: 1.27 msec per loop
# "task1.main_with_loops(10000)"
# 100 loops, best of 3: 12.6 msec per loop
# "task1.main_with_loops(100000)"
# 100 loops, best of 3: 125 msec per loop



# 2) Нахождение суммы элементов множества от a_id до b_id рекурсивно

def interval_sum_rec(a_id, b_id, array):

    if (b_id - a_id) == 2:  # один элемент между min и max - базовый случай
        return array[a_id + 1]
    else:
        return array[a_id + 1] + interval_sum_rec(a_id + 1, b_id, array)


def main_with_rec(size):

    numbers = get_array(size)

    max_id = 0
    min_id = 0
    for i in range(1, size):
        if numbers[i] > numbers[max_id]:
            max_id = i
        if numbers[i] < numbers[min_id]:
            min_id = i

    if abs(min_id - max_id) == 1:
        return 0
    elif max_id > min_id:
        return interval_sum_rec(min_id, max_id, numbers)
    else:
        return interval_sum_rec(max_id, min_id, numbers)


# cProfile.run('main_with_rec(1000)')
#         1    0.000    0.000    0.002    0.002 task1.py:13(get_array)
#     543/1    0.001    0.000    0.001    0.001 task1.py:65(interval_sum_rec)
#         1    0.000    0.000    0.003    0.003 task1.py:73(main_with_rec)
#
# cProfile.run('main_with_rec(100)')
#         1    0.000    0.000    0.000    0.000 task1.py:13(get_array)
#       5/1    0.000    0.000    0.000    0.000 task1.py:65(interval_sum_rec)
#         1    0.000    0.000    0.000    0.000 task1.py:73(main_with_rec)
#
# cProfile.run('main_with_rec(10)')
#         1    0.000    0.000    0.000    0.000 task1.py:13(get_array)
#       4/1    0.000    0.000    0.000    0.000 task1.py:65(interval_sum_rec)
#         1    0.000    0.000    0.000    0.000 task1.py:73(main_with_rec)


# "task1.main_with_rec(10)"
# 100 loops, best of 3: 19.6 usec per loop
# "task1.main_with_rec(100)"
# 100 loops, best of 3: 123 usec per loop
# "task1.main_with_rec(1000)"
# 100 loops, best of 3: 1.15 msec per loop



"""
Имеет смысл сравнить функции получения суммы элементов массива в интервале, для этого напишем "обертки":
test_interval_sum_loops(), test_interval_sum_rec()

 - генерируем массив длинной TEST_SIZE = 1000000, чтобы занимал одинаковый объем памяти при разных интервалах
 - считаем суммы по интервалам (0, n), n - варьируем
 
 
Вывод по результатам замеров cProfile:
однозначно стоит отказаться от использования рекурсии для посчета суммы элементов,
не только из соображений скорости, но и из-за опасности выйти за допустимое значение глубины рекурсии
при неудачных положениях min и max элементов в больших массивах (SIZE => 1000)

"""

TEST_SIZE = 1000000

def test_interval_sum_loops(interval_size):

    numbers = get_array(TEST_SIZE)
    return interval_sum_loops(0, interval_size, numbers)

# cProfile.run('test_interval_sum_loops(1000)')

#        1    0.000    0.000    0.000    0.000 task1.py:27(interval_sum_loops) - 1000
#        1    0.001    0.001    0.001    0.001 task1.py:27(interval_sum_loops) - 10000
#        1    0.003    0.003    0.003    0.003 task1.py:27(interval_sum_loops) - 50000
#        1    0.005    0.005    0.005    0.005 task1.py:27(interval_sum_loops) - 100000
#        1    0.028    0.028    0.028    0.028 task1.py:27(interval_sum_loops) - 500000
#        1    0.055    0.055    0.055    0.055 task1.py:27(interval_sum_loops) - 999999



def test_interval_sum_rec(interval_size):

    numbers = get_array(TEST_SIZE)
    return interval_sum_rec(0, interval_size, numbers)

# cProfile.run('test_interval_sum_rec(980)')

#      9/1    0.000    0.000    0.000    0.000 task1.py:65(interval_sum_rec) - 10
#    499/1    0.000    0.000    0.000    0.000 task1.py:65(interval_sum_rec) - 500
#    899/1    0.014    0.000    0.014    0.014 task1.py:65(interval_sum_rec) - 900
#    979/1    0.012    0.000    0.012    0.012 task1.py:65(interval_sum_rec) - 980



# 3) Нахождение суммы элементов множества от a_id до b_id в цикле, + встроенные функции

def main_with_loop_standard_funcs(size):

    numbers = get_array(size)

    max_id = numbers.index(max(numbers))
    min_id = numbers.index(min(numbers))

    if abs(min_id - max_id) == 1:
        return 0
    elif max_id > min_id:
        return interval_sum_loops(min_id, max_id, numbers)
    else:
        return interval_sum_loops(max_id, min_id, numbers)


# cProfile.run('main_with_loop_standard_funcs(1000)')
#         1    0.000    0.000    0.003    0.003 task1.py:13(get_array)
#         1    0.000    0.000    0.003    0.003 task1.py:136(main_with_loop_standard_funcs)
#         1    0.000    0.000    0.000    0.000 task1.py:27(interval_sum_loops)
#
# cProfile.run('main_with_loop_standard_funcs(10000)')
#         1    0.000    0.000    0.026    0.026 task1.py:13(get_array)
#         1    0.000    0.000    0.026    0.026 task1.py:136(main_with_loop_standard_funcs)
#         1    0.000    0.000    0.000    0.000 task1.py:27(interval_sum_loops)
#
# cProfile.run('main_with_loop_standard_funcs(100000)')
#         1    0.000    0.000    0.199    0.199 task1.py:13(get_array)
#         1    0.000    0.000    0.203    0.203 task1.py:136(main_with_loop_standard_funcs)
#         1    0.001    0.001    0.001    0.001 task1.py:27(interval_sum_loops)
#
# cProfile.run('main_with_loop_standard_funcs(500000)')
#         1    0.000    0.000    1.031    1.031 task1.py:13(get_array)
#         1    0.000    0.000    1.056    1.056 task1.py:136(main_with_loop_standard_funcs)
#         1    0.005    0.005    0.005    0.005 task1.py:27(interval_sum_loops)


# "task1.main_with_loop_standard_funcs(10)"
# 100 loops, best of 3: 19.7 usec per loop
# "task1.main_with_loop_standard_funcs(100)"
# 100 loops, best of 3: 125 usec per loop
# "task1.main_with_loop_standard_funcs(1000)"
# 100 loops, best of 3: 1.18 msec per loop
# "task1.main_with_loop_standard_funcs(10000)"
# 100 loops, best of 3: 12 msec per loop
# "task1.main_with_loop_standard_funcs(100000)"
# 100 loops, best of 3: 116 msec per loop

"""
Выводы: 
1) показано, что использование рекурсии для подсчета суммы элементов массива на больших массивах приведет к выходу за 
    максимальные значения глубины рекурсии
2) для реализации подсчета суммы элементов с помощью цикла, показано, что использование стандартных функций поиска
    min и max значений при увеличении длины исходного массива позволяют немного ускорить работу программы, несмотря на
    то, что при вызове numbers.index(max(numbers)) кажется, выполняется 2 "прохода" по массиву (поиск max и нахождение 
    его индекса). Но засчет того, что эти встроенные функции на самом деле не перебирают массивы целиком, наблюдается 
    увеличесние скорости.
    
Поскольку в программе нет вложенных циклов, я бы сказала, что сложность алгоритма линейная O(n).
"""