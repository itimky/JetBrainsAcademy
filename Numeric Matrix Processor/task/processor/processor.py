def m_print(m):
    print('The result is:')
    for i in m:
        print(*i)


def m_create(count=''):
    rows, columns = [int(i) for i in input('Enter size of {}: '.format(count)).split()]
    print('Enter {}:'.format(count))
    m = [[int(i) if i.isdigit() else float(i) for i in input().split()] for _ in range(rows)]
    return m


def m_sum():
    m_a = m_create('first matrix')
    m_b = m_create('second matrix')

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
    m = m_create('matrix')
    c = int(input('Enter constant: '))
    res = [[element * c for element in row] for row in m]
    m_print(res)


def m_mul():
    m_a = m_create('first matrix')
    m_b = m_create('second matrix')

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
    m = m_create('matrix')

    if trans == 1:
        res = [[m[row][column] for row in range(len(m[0]))] for column in range(len(m))]
        m_print(res)

    elif trans == 2:
        res = [[m[row][column] for row in reversed(range(len(m[0])))] for column in reversed(range(len(m)))]
        m_print(res)

    elif trans == 3:
        res = [row[::-1] for row in m]
        m_print(res)

    elif trans == 4:
        res = [row for row in reversed(m)]
        m_print(res)


def minor(m, x, y):
    res = []
    for i in m[:x] + m[x + 1:]:
        row = []
        for j in i[:y] + i[y + 1:]:
            row.append(j)
        res.append(row)
    return det(res)


def cofactor(m, x, y):
    return (-1) ** (x + y) * minor(m, x, y)


def det(m):
    if len(m) == 1:
        return m[0][0]
    elif len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    else:
        return sum(element * cofactor(m, 0, j) for j, element in enumerate(m[0]))


def m_det():
    m = m_create('matrix')
    if len(m) == len(m[0]):
        print('The result is:', det(m), sep='\n')
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
