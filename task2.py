"""

Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""

from collections import deque


def prepare_sum_utils():
    DIGITS = [str(i) for i in range(10)]
    DIGITS.extend(['a', 'b', 'c', 'd', 'e', 'f'])
    DIGITS.extend(str(i) for i in range(10,20))
    DIGITS.extend(['1a', '1b', '1c', '1d', '1e', '1f'])

    sum_matrix = []
    for i in range(16):
        sum_matrix.append(DIGITS[i : i + 16])

    # for i in sum_matrix:
    #     print(i)

    matrix_index_dict = dict(zip(DIGITS[:16], [i for i in range(16)]))  # для получения индекса в матрице сложения

    return DIGITS, sum_matrix, matrix_index_dict


def prepare_mult_utils(DIGITS):

    mult_matrix = [['0' for i in range(16)] for j in range(16)]
    for i in range(1, 16):
        for j in range(16):
            mult_matrix[i][j] = ''.join(numbers_sum(DIGITS[j], mult_matrix[i - 1][j]))

    # for line in mult_matrix:
    #     print(line)

    return mult_matrix


def numbers_sum(a_number, b_number):

    sum_res = deque()
    add_prev = []

    a_d = deque(a_number)
    b_d = deque(b_number)

    for i in range(max(len(a_d), len(b_d))+1):
        if len(a_d) > 0:
            a = MATRIX_INDEX_DICT[a_d.pop()]
        else:
            a = 0
        if len(b_d) >0:
            b = MATRIX_INDEX_DICT[b_d.pop()]
        else:
            b = 0

        # print(a,b)

        res = list(SUM_MATRIX[a][b])
        # print(res)
        if len(add_prev) > 0:
            # res = list(sum_matrix[matrix_index_dict[add_prev.pop()]][matrix_index_dict[res]]) # проблемка, res тоже двузначный может быть
            # print(f'ATTENTION {res}')
            res = list(DIGITS[DIGITS.index(''.join(res)) + 1]) # костыль

            # print(f'перенесли разряд {res}')

        sum_res.appendleft(res.pop())

        # print(sum_res)

        if len(res) > 0:
            add_prev = list(res.pop())
            # print(f'add_prev {add_prev}')
        else:
            add_prev = []
            # print('обнулили add_prev')

    if sum_res[0] == '0':
        sum_res.popleft()

    # print(f'Сумма: {sum_res}')
    return list(sum_res)


def numbers_mult(a_number, b_number):

    mult_res = []
    res = []
    add_prev = []

    a_d = deque(a_number)

    for i in range(len(a_d)):

        a = MATRIX_INDEX_DICT[a_d.pop()]
        res = []
        b_d = deque(b_number)
        for j in range(len(b_d)):
            b = MATRIX_INDEX_DICT[b_d.pop()]
            res = numbers_sum(list(MULT_MATRIX[a][b]) + ['0'] * j, res)
        # print(f'res {res}')

        mult_res = numbers_sum(res + ['0'] * i, mult_res)
        # print(f'mult_res {mult_res}')

    mult_res = deque(mult_res)

    while (mult_res[0] == '0') and (mult_res != deque(['0'])):
        mult_res.popleft()
        # print(f'multres {mult_res}')
    return list(mult_res)


# Быстрая проверка вычислений
def test_operations():
    import random
    exitcode = 0

    for i in range(1000):

        a, b = random.randint(0, 1000), random.randint(0, 1000)
        # a, b = 110, 289
        ahex, bhex = map(hex, [a, b])

        # print(a, b)


        if list(numbers_sum(list(ahex)[2:], list(bhex)[2:])) != list(hex(a + b))[2:]:
            print(f'SUM FAILED {ahex}, {bhex}')
            exitcode += 1

        if list(numbers_mult(list(ahex)[2:], list(bhex)[2:])) != list(hex(a * b))[2:]:
             print(f'MULT FAILED {ahex}, {bhex}')
             exitcode += 1

    print(f'exitcode {exitcode}')
    return


# Долго, но, вроде, надежно проверяет вычисления. На случай наступления паранойи.
def test_operations_full():
    exitcode = 0
    for i in range(1000):
        for j in range(100):
            a, b = i, j
            # a, b = 110, 289
            ahex, bhex = map(hex, [a, b])

            # print(a, b)

            if list(numbers_sum(list(ahex)[2:], list(bhex)[2:])) != list(hex(a + b))[2:]:
                print(f'SUM FAILED {ahex}, {bhex}')
                exitcode += 1

            if list(numbers_mult(list(ahex)[2:], list(bhex)[2:])) != list(hex(a * b))[2:]:
                print(f'MULT FAILED {ahex}, {bhex}')
                exitcode += 1

    print(f'exitcode {exitcode}')
    return



DIGITS, SUM_MATRIX, MATRIX_INDEX_DICT = prepare_sum_utils()
MULT_MATRIX = prepare_mult_utils(DIGITS)

# a_number = list('0')
# b_number = list('c4')

# a_number = list(input('Введите число а (c 0x):').lower())[2:]
# b_number = list(input('Введите число b (c 0x):').lower())[2:]

a_number = list(input('Введите число а (без 0x):').lower())
b_number = list(input('Введите число b (без 0x):').lower())

s = numbers_sum(a_number, b_number)
m = numbers_mult(a_number, b_number)

print(f'Сумма: {"".join(s)}, Произведение: {"".join(m)}')


