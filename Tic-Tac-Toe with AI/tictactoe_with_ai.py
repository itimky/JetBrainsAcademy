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
        self.turn = 'X'
        self.opp_turn = 'O'

    def print_state(self):
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
            return f'{command[1] + (" AI" if command[1] != "user" else ("" if command[2] != "user" else " 1"))} wins'
        elif wins == 'O':
            return f'{command[2] + (" AI" if command[2] != "user" else ("" if command[1] != "user" else " 2"))} wins'
        else:
            return 'Wrong state!'

    def validate_input(self, x_y):
        """
        Validating user input: 2 integers from 1 to 3 separated by a space
        """
        if x_y[0].isdigit() and x_y[2].isdigit:
            if 0 < int(x_y[0]) < 4 and 0 < int(x_y[2]) < 4:
                if self.state[self.POSITION[x_y]] == ' ':
                    return True
                else:
                    print('This cell is occupied! Choose another one!')
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')
        return False

    def change_turn(self):
        self.turn, self.opp_turn = self.opp_turn, self.turn

    def easy(self):
        """
        easy AI, just random moves
        """
        self.state[random.choice(TicTacToe.empty_indexes(self.state))] = self.turn
        self.change_turn()
        return f'Making move level "easy" with "{self.opp_turn}"'

    def ready_to_win(self, xo):
        """
        helper function for medium AI, determines is X o O player ready to vin in one move
        """
        for pos in self.MEANINGFUL_POSITIONS:
            line = self.state[pos[0]] + self.state[pos[1]] + self.state[pos[2]]
            if line.count(xo) == 2 and ' ' in line:
                return str(pos[line.index(' ')])
        return

    def medium(self):
        """
        medium AI, if two Xs or Os in one line it uses it, otherwise random move
        """
        if self.ready_to_win(self.turn):
            self.state[int(self.ready_to_win(self.turn))] = self.turn
            self.change_turn()
            return f'Making move level "medium" with "{self.turn}"'
        elif self.ready_to_win(self.opp_turn):
            self.state[int(self.ready_to_win(self.opp_turn))] = self.turn
            self.change_turn()
            return f'Making move level "medium" with "{self.turn}"'
        self.state[random.choice(TicTacToe.empty_indexes(self.state))] = self.turn
        self.change_turn()
        return f'Making move level "medium" with "{self.opp_turn}"'

    def hard(self):
        """
        hard AI, check for best move in pickles.txt, if not found: use minimax on every possible move
        randomly select from the best moves, add best moves to pickles.txt
        """
        with open('pickles.txt', 'a+') as file:
            file.seek(0, 0)
            for line in file:
                if ','.join(str(i) for i in self.state) in line:
                    best_moves = [int(i) for i in line.split(';')[1].rstrip().split(',')]
                    file.seek(0, 2)
                    break
            else:
                new_state = self.state[:]
                moves = [' '] * 9
                for idx in TicTacToe.empty_indexes(self.state):
                    new_state[idx] = self.turn
                    moves[idx] = TicTacToe.min_max(new_state, self.turn)
                    new_state[idx] = ' '
                best_moves = [i for i, n in enumerate(moves) if (n == 1
                                                                 or n == 0 and 1 not in moves
                                                                 or n == -1 and 1 not in moves and 0 not in moves)]
                file.write(','.join(str(i) for i in self.state) + ';' + ','.join(str(i) for i in best_moves) + '\n')
        self.state[random.choice(best_moves)] = self.turn
        self.change_turn()
        return f'Making move level "hard" with "{self.opp_turn}"'

    @staticmethod
    def empty_indexes(state):
        return [i for i, idx in enumerate(state) if idx == ' ']

    @staticmethod
    def min_max(state, xo):
        """
        minimax recursive function. goes all over the tree, MAX on player turn, MIN on opponent turn
        """
        changing_xo = 'X' if state.count('X') == state.count('O') else 'O'
        win = TicTacToe.min_max_win(state, xo)
        if win:
            return win
        elif len(TicTacToe.empty_indexes(state)) == 0:
            return 0
        scores = []
        new_state = state[:]
        for idx in TicTacToe.empty_indexes(state):
            new_state[idx] = changing_xo
            scores.append(TicTacToe.min_max(new_state, xo))
            new_state[idx] = ' '
        return max(scores) if changing_xo == xo else min(scores)

    @staticmethod
    def min_max_win(state, xo):
        """
        helper function for minimax,
        returns +1 if X (or O) already wins and -1 if O (or X) already wins
        """
        for pos in TicTacToe.MEANINGFUL_POSITIONS:
            if state[pos[0]] == state[pos[1]] == state[pos[2]]:
                if state[pos[0]] == xo:
                    return 1
                elif state[pos[0]] != ' ':
                    return -1
        return False

    def user(self):
        """
        get coordinates from user, validate it, and make a move
        """
        while True:
            x_y = input(f'Enter the coordinates for "{self.turn}" (x y): ')
            if self.validate_input(x_y):
                self.state[self.POSITION[x_y]] = self.turn
                self.change_turn()
                return f'Placing {self.opp_turn}'

    def start(self):
        possible_players = {'user': self.user, 'easy': self.easy,
                            'medium': self.medium, 'hard': self.hard}
        print('''
possible commands:
"start <player1> <player2>"
"exit"

possible players:
"user" "easy" "medium" "hard"

coordinates are in form "x y"
"x" - columns, "y" - rows
"1 1" - left bottom corner     
              ''')
        self.print_state()
        while True:
            self.state = [' '] * 9
            self.turn = 'X'
            self.opp_turn = 'O'
            command = input('Input command: ').split()
            if command[0] == 'start' and command[1] in possible_players and command[2] in possible_players:
                while True:
                    print(possible_players[command[1]]())
                    self.print_state()
                    print()
                    if self.state_analyze(command) != 'Game not finished':
                        print(self.state_analyze(command) + '\n')
                        break
                    print(possible_players[command[2]]())
                    self.print_state()
                    print()
                    if self.state_analyze(command) != 'Game not finished':
                        print(self.state_analyze(command) + '\n')
                        break
            elif command[0] == 'exit':
                break
            else:
                print('Bad parameters!')


game = TicTacToe()
game.start()
