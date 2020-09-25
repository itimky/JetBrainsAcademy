import random


class TicTacToe:

    MEANINGFUL_POSITIONS = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows, columns, diagonals
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6))
    POSITION = {'1 3': 0, '2 3': 1, '3 3': 2,  # translating x,y coordinates to position in state list
                '1 2': 3, '2 2': 4, '3 2': 5,
                '1 1': 6, '2 1': 7, '3 1': 8, }

    def __init__(self):
        self.state = [' '] * 9

    def __str__(self):
        print('y^--------')
        print('3|', self.state[0], self.state[1], self.state[2], '|')
        print('2|', self.state[3], self.state[4], self.state[5], '|')
        print('1|', self.state[6], self.state[7], self.state[8], '|')
        print(' -------->x')
        print('   1 2 3')

    def state_analyze(self, command):
        """
        Checking state of the game.
        """
        wins = ''
        for pos in self.MEANINGFUL_POSITIONS:
            if self.state[pos[0]] == self.state[pos[1]] == self.state[pos[2]] \
                    and self.state[pos[0]] != ' ':
                wins += self.state[pos[0]]
        if wins == '' and ' ' in self.state:
            return 'Game not finished'
        elif wins == '' and ' ' not in self.state:
            return 'Draw'
        elif wins == 'X':
            return f'{command[1] + " AI" if command[1] != "user" else ""} wins'
        elif wins == 'O':
            return f'{command[2] + " AI" if command[2] != "user" else ""} wins'
        else:
            return 'Wrong state!'

    def validate_input(self, x_y):
        """
        Validating user input: 2 integers from 1 to 3 separated by a space
        """
        if x_y[0].isdigit() and x_y[1].isdigit:
            if 0 < int(x_y[0]) < 4 and 0 < int(x_y[1]) < 4:
                if self.state[self.POSITION[x_y]] == ' ':
                    return True
                else:
                    print('This cell is occupied! Choose another one!')
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')
        return False
    



    def easy(state):
        xo = x_or_o(state)
        print(f'Making move level "easy" with "{xo}"')
        empty_cell_list = [i for i, item in enumerate(state) if item == ' ']
        state[random.choice(empty_cell_list)] = xo
        return state


    def medium(state):
        xo = x_or_o(state)
        print(f'Making move level "medium" with "{xo}"')
        ox = 'X' if xo == 'O' else 'O'
        if is_winning(state, xo):
            state[int(is_winning(state, xo))] = xo
            return state
        elif is_winning(state, ox):
            state[int(is_winning(state, ox))] = xo
            return state
        empty_cell_list = [i for i, item in enumerate(state) if item == ' ']
        state[random.choice(empty_cell_list)] = xo
        return state


    def hard(state):
        xo = x_or_o(state)
        print(f'Making move level "hard" with "{xo}"')
        with open('pickles.txt', 'a+') as file:
            file.seek(0, 0)
            for line in file:
                if ','.join(str(i) for i in state) in line:
                    best_moves = [int(i) for i in line.split(';')[1].rstrip().split(',')]
                    file.seek(0, 2)
                    break
            else:
                new_state = state[:]
                moves = [' '] * 9
                for idx in empty_indexes(state):
                    new_state[idx] = xo
                    moves[idx] = min_max(new_state, xo)
                    new_state[idx] = ' '
                best_moves = [i for i, n in enumerate(moves) if (n == 1
                                                                 or n == 0 and 1 not in moves
                                                                 or n == -1 and 1 not in moves and 0 not in moves)]
                file.write(','.join(str(i) for i in state) + ';' + ','.join(str(i) for i in best_moves) + '\n')
        state[random.choice(best_moves)] = xo
        return state


    def min_max(state, sign):
        xo = x_or_o(state)
        win = min_max_win(state, sign)
        if win:
            return win
        elif len(empty_indexes(state)) == 0:
            return 0
        scores = []
        new_state = state[:]
        for idx in empty_indexes(state):
            new_state[idx] = xo
            scores.append(min_max(new_state, sign))
            new_state[idx] = ' '
        return max(scores) if xo == sign else min(scores)


    def min_max_win(state, sign):
        for pos in self.MEANINGFUL_POSITIONS:
            if state[pos[0]] == state[pos[1]] == state[pos[2]]:
                if state[pos[0]] == sign:
                    return 1
                elif state[pos[0]] != ' ':
                    return -1
        return False


    def empty_indexes(state):
        return [i for i, idx in enumerate(state) if idx == ' ']


    def is_winning(state, xo):
        for pos in self.MEANINGFUL_POSITIONS:
            line = state[pos[0]] + state[pos[1]] + state[pos[2]]
            if line.count(xo) == 2 and ' ' in line:
                return str(pos[line.index(' ')])
        return


    def user(state):
        xo = x_or_o(state)
        while True:
            x_y = input(f'Enter the coordinates for "{xo}" (x y): ').split()
            if validate_input(x_y):
                state[self.POSITION[x_y]] = x_or_o(state)
                return state


    def x_or_o(state):
        if state.count('X') == state.count('O'):
            return 'X'
        elif state.count('X') > state.count('O'):
            return 'O'
    

game = TicTacToe()

def main():
    possible_players = {'user': user, 'easy': easy, 'medium': medium, 'hard': hard}
    while True:
        command = input('Input command: ').split()
        if command[0] == 'start' and command[1] in possible_players and command[2] in possible_players:
            state = [' '] * 9
            while True:
                state = possible_players[command[1]](state)
                print(game)
                print()
                if state_analyze(state, command) != 'Game not finished':
                    print(state_analyze(state, command) + '\n')
                    break
                state = possible_players[command[2]](state)
                print(game)
                print()
                if state_analyze(state, command) != 'Game not finished':
                    print(state_analyze(state, command) + '\n')
                    break
        elif command[0] == 'exit':
            break
        else:
            print('Bad parameters!')


if __name__ == '__main__':
    main()
