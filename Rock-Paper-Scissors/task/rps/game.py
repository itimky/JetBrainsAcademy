import random


def win(first_move, second_move, options):
    if first_move in options and second_move in options:
        if first_move == second_move:
            return 'draw'
        else:
            precedence = options[options.index(first_move) + 1:] + options[:options.index(first_move)]
            if precedence.index(second_move) + 1 > len(precedence) / 2:
                return 'first'
            else:
                return 'second'
    else:
        print('Move not in options')
        return None


def pc_move(options):
    return random.choice(options)


def main():
    name = input('Enter your name: ')
    print('Hello,', name)
    score = 0
    with open('rating.txt') as f:
        for line in f:
            if line.split()[0] == name:
                score = int(line.split()[1])

    options = input().split(',')
    if options == ['']:
        options = ['rock', 'paper', 'scissors']

    print("Okay, let's start")
    while True:
        command = input()
        pc_hand = pc_move(options)

        if command[0] == '!':
            if command == '!exit':
                print('Bye!')
                exit()
            elif command == '!rating':
                print('Your rating:', score)
            else:
                print('Invalid input')
        else:
            winner = win(command, pc_hand, options)
            if winner == 'first':
                print('Well done. The computer chose {} and failed'.format(pc_hand))
                score += 100
            elif winner == 'second':
                print('Sorry, but the computer chose {}'.format(pc_hand))
            elif winner == 'draw':
                print('There is a draw {}'.format(pc_hand))
                score += 50
            else:
                print('Invalid input')


if __name__ == '__main__':
    main()
