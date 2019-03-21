from collections import Counter

class MyNode:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def is_terminal(self):
        return (self.left is not None) + (self.right is not None) == 0


def get_tree(string):
    symbols = sorted(dict(Counter(string)).items(), key=lambda x: x[1])
    symbols = [list(elem) for elem in symbols]
    for symbol in symbols:
        symbol[0] = MyNode(symbol[0])

    unique_symbols_count = len(symbols)

    i = 1
    while len(symbols) > 1:
        symbols = sorted(symbols, key=lambda x: x[1])
        node = MyNode(value=f'node{i}', left=symbols[0][0], right=symbols[1][0])
        symbols[0][0].parent = node
        symbols[1][0].parent = node

        symbols.append((node, sum([x[1] for x in symbols[:2]])))
        del symbols[:2]
        i += 1
        # print(symbols)
    return node, unique_symbols_count


def get_pathes(node, symbols_table, path=''):
    if len(node.value) == 1:
        print(f'символ {node.value} - {path}')
        symbols_table[node.value] = path

        if node.parent.right is not None:
            node.parent.right = None
        elif node.parent.left is not None:
            node.parent.left = None
        return

    if node.right is not None and len(node.right.value) > 1 and node.right.is_terminal():
        # print(f'delete {node.right.value}')
        node.right = None
    if node.left is not None and len(node.left.value) > 1 and node.left.is_terminal():
        # print(f'delete {node.left.value}')
        node.left = None

    if node.right is not None:
        # print(node.right, path)
        return get_pathes(node.right, symbols_table, path + '1')
    if node.left is not None:
        # print(node.left, path)
        return get_pathes(node.left, symbols_table, path + '0')

def get_symbols_table(node):
    symbols_table = {}
    while not node.is_terminal():
        get_pathes(node, symbols_table)
    return symbols_table


#input_string = 'tree pass ttttrrphgjuj'
input_string = input('Введите строку: ')

node, unique_symbols_count = get_tree(input_string)

symbols_table = get_symbols_table(node)
coded_string = ' '.join([symbols_table[x] for x in input_string ])

print(coded_string)