"""

Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""

from collections import deque, namedtuple

DIGITS = [str(i) for i in range(10)]
DIGITS.extend(['a', 'b', 'c', 'd', 'e', 'f'])
DIGITS.extend(str(i) for i in range(10,20))
DIGITS.extend(['1a', '1b', '1c', '1d', '1e', '1f'])

sum_matrix = []
for i in range(16):
    sum_matrix.append(DIGITS[i : i + 16])

for i in sum_matrix:
    print(i)

matrix_index_dict = dict(zip(DIGITS[:16], [i for i in range(16)])) # для получения индекса в матрице сложения





sum_res = deque()
res = []
add_prev = []



a_number = list('ff')
b_number = list('aff')

a_d = deque(a_number)
b_d = deque(b_number)

for i in range(len(a_d)+1):
    if len(a_d) > 0:
        a = matrix_index_dict[a_d.pop()]
    else:
        a = 0
    if len(b_d) >0:
        b = matrix_index_dict[b_d.pop()]
    else:
        b = 0

    print(a,b)

    res = list(sum_matrix[a][b])
    print(res)
    if len(add_prev) > 0:
        # res = list(sum_matrix[matrix_index_dict[add_prev.pop()]][matrix_index_dict[res]]) # проблемка, res тоже двузначный может быть
        res = list(DIGITS[matrix_index_dict[res.pop()] + 1]) # костыль
        print(f'перенесли разряд {res}')

    sum_res.appendleft(res.pop())

    print(sum_res)

    if len(res) > 0:
        add_prev = list(res.pop())
        print(f'add_prev {add_prev}')
    else:
        add_prev = []
        print('обнулили add_prev')

print(f'Сумма: {sum_res}')


