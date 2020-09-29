import random


class TicTacToe:
    MEANINGFUL_POSITIONS = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows, columns, diagonals
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6))

    def __init__(self):
        self.state = [' '] * 9
        self.turn = 'X'
        self.opp_turn = 'O'
        self.player = None
        self.next_player = None

    def reset(self):
        self.state = [' '] * 9
        self.turn = 'X'
        self.opp_turn = 'O'
        self.player = None
        self.next_player = None

    def get_state(self):
        return self.state

    def get_xo(self):
        return self.turn

    def set_state(self, state):
        self.state = state

    def set_players(self, player1, player2):
        self.player = player1
        self.next_player = player2

    def player(self):
        return self.player

    def print_state(self):
        print('y^--------')
        print('3|', self.state[0], self.state[1], self.state[2], '|')
        print('2|', self.state[3], self.state[4], self.state[5], '|')
        print('1|', self.state[6], self.state[7], self.state[8], '|')
        print(' -------->x')
        print('   1 2 3')

    def state_analyze(self, command):
        """
        Checking state of the game. Defining is the game finished and how
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

    def change_turn(self):
        self.turn, self.opp_turn = self.opp_turn, self.turn
        self.player, self.next_player = self.next_player, self.player


class TicTacToeUser:
    POSITION = {'1 3': 0, '2 3': 1, '3 3': 2,  # translating x,y coordinates to position in state list
                '1 2': 3, '2 2': 4, '3 2': 5,
                '1 1': 6, '2 1': 7, '3 1': 8, }

    @staticmethod
    def make_move(state, xo):
        """
        get coordinates from user, validate it, and make a move
        """
        while True:
            x_y = input(f'Enter the coordinates for "{xo}" (x y): ')
            if TicTacToeUser.validate_input(state, x_y):
                state[TicTacToeUser.POSITION[x_y]] = xo
                return state

    @staticmethod
    def validate_input(state, x_y):
        """
        Validating user input: 2 integers from 1 to 3 separated by a space
        """
        if len(x_y) == 3 and x_y[0].isdigit() and x_y[2].isdigit:
            if 0 < int(x_y[0]) < 4 and 0 < int(x_y[2]) < 4:
                if state[TicTacToeUser.POSITION[x_y]] == ' ':
                    return True
                else:
                    print('This cell is occupied! Choose another one!')
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter two numbers!')
        return False


class TicTacToeAI:
    MEANINGFUL_POSITIONS = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows, columns, diagonals
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6))

    @staticmethod
    def empty_indexes(state):
        return [i for i, idx in enumerate(state) if idx == ' ']


class TicTacToeEasyAI(TicTacToeAI):

    @staticmethod
    def make_move(state, xo):
        """
        easy AI, just random moves
        """
        state[random.choice(TicTacToeAI.empty_indexes(state))] = xo
        print(f'Making move level "easy" with "{xo}"')
        return state


class TicTacToeMediumAI(TicTacToeAI):

    @staticmethod
    def make_move(state, xo):
        """
        medium AI, if two Xs or Os in one line it uses it, otherwise random move
        """
        ox = 'O' if xo == 'X' else 'X'
        if TicTacToeMediumAI.ready_to_win(state, xo):
            state[int(TicTacToeMediumAI.ready_to_win(state, xo))] = xo
            print(f'Making move level "medium" with "{xo}"')
            return state
        elif TicTacToeMediumAI.ready_to_win(state, ox):
            state[int(TicTacToeMediumAI.ready_to_win(state, ox))] = xo
            print(f'Making move level "medium" with "{xo}"')
            return state
        state[random.choice(TicTacToeAI.empty_indexes(state))] = xo
        print(f'Making move level "medium" with "{xo}"')
        return state

    @staticmethod
    def ready_to_win(state, xo):
        """
        helper function for medium AI, determines is X o O player ready to vin in one move
        """
        for pos in TicTacToeAI.MEANINGFUL_POSITIONS:
            line = state[pos[0]] + state[pos[1]] + state[pos[2]]
            if line.count(xo) == 2 and ' ' in line:
                return str(pos[line.index(' ')])
        return


class TicTacToeHardAI(TicTacToeAI):
    BEST_MOVES_FILE = 'pickles.txt'

    def __init__(self):
        self.pickles = {}
        with open(TicTacToeHardAI.BEST_MOVES_FILE, 'a+', encoding='utf-8') as f:
            for line in f:
                best_moves = [int(i) for i in line.split(';')[1].rstrip().split(',')]
                position = [str(i) for i in line.split(';')[0].split(',')]
                self.pickles[tuple(position)] = best_moves

    def make_move(self, state, xo):
        """
        hard AI, check for best move in pickles.txt, if not found: use minimax on every possible move
        randomly select from the best moves, add best moves to pickles.txt
        """

        if tuple(state) in self.pickles:
            best_moves = self.pickles[tuple(state)]
        else:
            new_state = state[:]
            moves = [' '] * 9
            for idx in TicTacToeAI.empty_indexes(state):
                new_state[idx] = xo
                moves[idx] = TicTacToeHardAI.min_max(new_state, xo)
                new_state[idx] = ' '
            best_moves = [i for i, n in enumerate(moves) if (n == 1
                                                             or n == 0 and 1 not in moves
                                                             or n == -1 and 1 not in moves and 0 not in moves)]
            self.pickles[tuple(state)] = best_moves
            with open('pickles.txt', 'a+') as file:
                file.write(','.join(str(i) for i in state) + ';' + ','.join(str(i) for i in best_moves) + '\n')
        state[random.choice(best_moves)] = xo
        print(f'Making move level "hard" with "{xo}"')
        return state

    @staticmethod
    def min_max(state, xo):
        """
        minimax recursive function. goes all over the tree, MAX on player turn, MIN on opponent turn
        """
        changing_xo = 'X' if state.count('X') == state.count('O') else 'O'
        win = TicTacToeHardAI.min_max_win(state, xo)
        if win:
            return win
        elif len(TicTacToeHardAI.empty_indexes(state)) == 0:
            return 0
        scores = []
        new_state = state[:]
        for idx in TicTacToeHardAI.empty_indexes(state):
            new_state[idx] = changing_xo
            scores.append(TicTacToeHardAI.min_max(new_state, xo))
            new_state[idx] = ' '
        return max(scores) if changing_xo == xo else min(scores)

    @staticmethod
    def min_max_win(state, xo):
        """
        helper function for minimax,
        returns +1 if X (or O) already wins and -1 if O (or X) already wins
        """
        for pos in TicTacToeAI.MEANINGFUL_POSITIONS:
            if state[pos[0]] == state[pos[1]] == state[pos[2]]:
                if state[pos[0]] == xo:
                    return 1
                elif state[pos[0]] != ' ':
                    return -1
        return False


def main():
    print('''
possible commands: "start <player1> <player2>", "exit"
possible players: "user", "easy", "medium", "hard"
coordinates are in form "x y" <x> - columns, <y> - rows, "1 1" - left bottom corner
"X" plays first
        ''')
    game = TicTacToe()
    user = TicTacToeUser()
    easy = TicTacToeEasyAI()
    medium = TicTacToeMediumAI()
    hard = TicTacToeHardAI()
    possible_players = {'user': user, 'easy': easy,
                        'medium': medium, 'hard': hard}
    while True:
        command = input('Input command: ').split()
        if command[0] == 'start' and command[1] in possible_players and command[2] in possible_players:
            if command[1] == 'user' or command[2] == 'user':
                game.print_state()
            game.set_players(possible_players[command[1]], possible_players[command[2]])
            while game.state_analyze(command) == 'Game not finished':
                game.set_state(game.player.make_move(game.get_state(), game.get_xo()))
                game.print_state()
                game.change_turn()
                print()
            print(game.state_analyze(command) + '\n')
            game.reset()
        elif command[0] == 'exit':
            break
        else:
            print('Bad parameters!')


if __name__ == '__main__':
    main()
