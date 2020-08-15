import random

name = input('Enter your name: ')
print('Hello,', name)

score = 0
f = open('rating.txt')
for line in f:
    if line.split()[0] == name:
        score = int(line.split()[1])

winning_moves = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
loosing_moves = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

player_hand = ''
while True:
    player_hand = input()
    computer_hand = random.choice(list(winning_moves.keys()))
    if player_hand == '!exit':
        print('Bye!')
        exit()
    elif player_hand == winning_moves[computer_hand]:
        print('Well done. The computer chose {} and failed'.format(computer_hand))
        score += 100
    elif player_hand == loosing_moves[computer_hand]:
        print('Sorry, but the computer chose {}'.format(computer_hand))
    elif player_hand == computer_hand:
        print('There is a draw {}'.format(computer_hand))
        score += 50
    elif player_hand == '!rating':
        print('Your rating:', score)
    else:
        print('Invalid input')
