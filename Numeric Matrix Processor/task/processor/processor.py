def m_print(m):
    print('The result is:')
    for i in m:
        print(*i)


def m_create(count=''):
    rows, columns = map(int, input('Enter size of {}matrix: '.format(count)).split())
    print('Enter {}matrix:'.format(count))
    m = []
    for i in range(rows):
        m.append(list(map(float, input().split())))
    return m
    #  rows, columns = [int(i) for i in input().split()]
    #  matrix = [[int(i) if i.isdigit() else float(i) for i in input().split()] for _ in range(rows)]


def m_sum():
    m_a = m_create('first ')
    m_b = m_create('second ')

    if len(m_a) == len(m_b) and len(m_a[0]) == len(m_b[0]):
        res = []
        for i in range(len(m_a)):
            row = []
            for j in range(len(m_a[0])):
                row.append(m_a[i][j] + m_b[i][j])
            res.append(row)
        m_print(res)
    else:
        print('The operation cannot be performed.')


def m_mul_const():
    m = m_create()
    c = int(input('Enter constant: '))

    res = []
    for i in range(len(m)):
        row = []
        for j in range(len(m[0])):
            row.append(m[i][j] * c)
        res.append(row)
    m_print(res)
    #  res = [[i*scalar for i in j] for j in matrix]


def m_mul():
    m_a = m_create('first ')
    m_b = m_create('second ')

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
        m_print(res)
    else:
        print('The operation cannot be performed.')


def m_trans():
    trans = int(input('1. Main diagonal\n'
                      '2. Side diagonal\n'
                      '3. Vertical line\n'
                      '4. Horizontal line\n'
                      'Your choice: '))
    m = m_create()

    if trans == 1:
        res = []
        for j in range(len(m[0])):
            row = []
            for i in range(len(m)):
                row.append(m[i][j])
            res.append(row)
        m_print(res)
    #  result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    elif trans == 2:
        res = []
        for j in reversed(range(len(m[0]))):
            row = []
            for i in reversed(range(len(m))):
                row.append(m[i][j])
            res.append(row)
        m_print(res)
    #  result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    #  result = [ele for ele in reversed(result)]
    #  result = [li[::-1] for li in result]

    elif trans == 3:
        res = []
        for i in m:
            res.append(reversed(i))
        m_print(res)
    #  result = [li[::-1] for li in matrix]

    elif trans == 4:
        res = []
        for i in reversed(m):
            res.append(i)
        m_print(res)
    #  result = [ele for ele in reversed(matrix)]


def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        return sum((-1) ** j * matrix[0][j] * det(sub_matrix(matrix, 0, j)) for j in range(len(matrix[0])))


def sub_matrix(matrix, x, y):
    res = []
    for i in matrix[:x] + matrix[x + 1:]:
        row = []
        for j in i[:y] + i[y + 1:]:
            row.append(j)
        res.append(row)
    return res


def m_det():
    m = m_create()
    if len(m) == len(m[0]):
        print('The result is:')
        print(det(m))
    else:
        print('The operation cannot be performed.')


def menu():
    while True:
        choice = input('\n1. Add matrices\n'
                       '2. Multiply matrix by a constant\n'
                       '3. Multiply matrices\n'
                       '4. Transpose matrix\n'
                       '5. Calculate a determinant\n'
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
        else:
            print('Wrong choice')


if __name__ == '__main__':
    menu()
