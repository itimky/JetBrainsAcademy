def print_state(state):
    print('---------')
    print('|' + state[0:3].replace('', ' ') + '|')
    print('|' + state[3:6].replace('', ' ') + '|')
    print('|' + state[6:9].replace('', ' ') + '|')
    print('---------')


def table_state(state):
    # 0-2 rows, 3-5 columns, 6-7 diagonals
    rows_cols_diagonals = [state[0] + state[1] + state[2],
                           state[3] + state[4] + state[5],
                           state[6] + state[7] + state[8],
                           state[0] + state[3] + state[6],
                           state[1] + state[4] + state[7],
                           state[2] + state[5] + state[8],
                           state[0] + state[4] + state[8],
                           state[2] + state[4] + state[6]]

    o_wins = 0
    x_wins = 0
    if abs(state.count('O') - state.count('X')) <= 1:
        for line in rows_cols_diagonals:
            if line == 'OOO':
                o_wins += 1
            elif line == 'XXX':
                x_wins += 1
        if x_wins == 1 and o_wins == 0:
            return 'X wins'
        elif o_wins == 1 and x_wins == 0:
            return 'O wins'
        elif o_wins == 0 and x_wins == 0 and '_' in state:
            return 'Game not finished'
        elif o_wins == 0 and x_wins == 0 and '_' not in state:
            return 'Draw'
        else:
            return 'Impossible'
    else:
        return 'Impossible'


board = '_________'
print_state(board)
round = 1
while True:
    coordinates = input('Enter the coordinates: ').split()
    if all(coordinate in '123' for coordinate in coordinates):
        place = 8 - 3 * int(coordinates[1]) + int(coordinates[0])
        if board[place] == '_':
            if round % 2 == 1:
                board = board[:place] + 'X' + board[place + 1:]
            else:
                board = board[:place] + 'O' + board[place + 1:]
            print_state(board)
            round += 1
            if table_state(board) in ('X wins', 'O wins', 'Draw'):
                print(table_state(board))
                break
        else:
            print('This cell is occupied! Choose another one!')
    else:
        if all(coordinate in '0123456789' for coordinate in coordinates):
            print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')
