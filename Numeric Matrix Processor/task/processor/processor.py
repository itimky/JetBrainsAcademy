def m_print(m):
    if len(m) == 1:
        print(m[0])
    else:
        print('The result is:')
        maximum = len(str(round(max([max(row) for row in m]))))
        int_matrix = all([type(m[i][j]) is int for i in range(len(m)) for j in range(len(m[0]))])
        if int_matrix:
            for row in m:
                for element in row:
                    print('{:{}d}'.format(element, maximum + 1), end=' ')
                print()
        else:
            for row in m:
                for element in row:
                    print('{:{}.3f}'.format(element, maximum + 5), end=' ')
                print()


def m_create(name=''):
    rows, columns = [int(i) for i in input('Enter size of {}: '.format(name)).split()]
    print('Enter {}:'.format(name))
    m = [[int(i) if i.isdigit() else float(i) for i in input().split()] for _ in range(rows)]
    return m


def sum_of_matrix(m_a, m_b):
    if len(m_a) == len(m_b) and len(m_a[0]) == len(m_b[0]):
        res = []
        for i in range(len(m_a)):
            row = []
            for j in range(len(m_a[0])):
                row.append(m_a[i][j] + m_b[i][j])
            res.append(row)
        return res
    else:
        return ['The operation cannot be performed.']


def multiply_by_constant(m, c):
    return [[element * c for element in row] for row in m]

    
def multiply_matrix(m_a, m_b):
    if len(m_a[0]) == len(m_b):
        res = []
        for i in range(len(m_a)):
            row = []
            for j in range(len(m_b[0])):
                element = 0
                for n in range(len(m_a[0])):
                    element += (m_a[i][n] * m_b[n][j])
                row.append(element)
            res.append(row)
        return res
    else:
        return ['The operation cannot be performed.']


def transpose_main(m):
    return [[m[row][column] for row in range(len(m[0]))] for column in range(len(m))]


def transpose_side(m):
    return [[m[row][column] for row in reversed(range(len(m[0])))] for column in reversed(range(len(m)))]


def transpose_vertical(m):
    return [row[::-1] for row in m]


def transpose_horizontal(m):
    return [row for row in reversed(m)]


def minor(m, x, y):
    res = []
    for i in m[:x] + m[x + 1:]:
        row = []
        for j in i[:y] + i[y + 1:]:
            row.append(j)
        res.append(row)
    return determinant(res)


def cofactor(m, x, y):
    return (-1) ** (x + y) * minor(m, x, y)


def determinant(m):
    if len(m) == 1:
        return m[0][0]
    elif len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    else:
        return sum(element * cofactor(m, 0, j) for j, element in enumerate(m[0]))


def inverse(m):
    if determinant(m) != 0:
        adj_m = []
        for i in range(len(m)):
            row = []
            for j in range(len(m[0])):
                row.append(cofactor(m, i, j))
            adj_m.append(row)
        res = multiply_by_constant(transpose_main(adj_m), 1 / determinant(m))
        return res
    else:
        return ['Matrix inverse does not exist']


def m_sum():
    m_a = m_create('first matrix')
    m_b = m_create('second matrix')
    m_print(sum_of_matrix(m_a, m_b))


def m_mul_const():
    m = m_create('matrix')
    c = int(input('Enter constant: '))
    m_print(multiply_by_constant(m, c))


def m_mul():
    m_a = m_create('first matrix')
    m_b = m_create('second matrix')
    m_print(multiply_matrix(m_a, m_b))


def m_trans():
    while True:
        trans = input('1. Main diagonal\n'
                      '2. Side diagonal\n'
                      '3. Vertical line\n'
                      '4. Horizontal line\n'
                      'Your choice: ')
        if trans == '1':
            m_print(transpose_main(m_create('matrix')))
            return
        elif trans == '2':
            m_print(transpose_side(m_create('matrix')))
            return
        elif trans == '3':
            m_print(transpose_vertical(m_create('matrix')))
            return
        elif trans == '4':
            m_print(transpose_horizontal(m_create('matrix')))
            return
        else:
            print('Wrong choice')


def m_det():
    m = m_create('matrix')
    if len(m) == len(m[0]):
        print('The result is:', determinant(m), sep='\n')
    else:
        print('The operation cannot be performed.')


def m_inv():
    m = m_create('matrix')
    m_print(inverse(m))


def menu():
    while True:
        choice = input('\n1. Add matrices\n'
                       '2. Multiply matrix by a constant\n'
                       '3. Multiply matrices\n'
                       '4. Transpose matrix\n'
                       '5. Calculate a determinant\n'
                       '6. Inverse matrix\n'
                       '0. Exit\n'
                       'Your choice: ')
        if choice == '0':
            exit()
        if choice == '1':
            m_sum()
        elif choice == '2':
            m_mul_const()
        elif choice == '3':
            m_mul()
        elif choice == '4':
            m_trans()
        elif choice == '5':
            m_det()
        elif choice == '6':
            m_inv()
        else:
            print('Wrong choice')


if __name__ == '__main__':
    menu()
