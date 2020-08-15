import random


def create_account():
    iin = '400000'
    can = ''
    for i in range(9):
        can += str(random.randint(0, 9))
    checksum = str(random.randint(0, 9))
    card_number = iin + can + checksum
    pin = ''
    for _ in range(4):
        pin += str(random.randint(1, 9))
    if card_number not in cards:
        cards[card_number] = pin
        balance[card_number] = 0
        print('\nYour card has been created\n'
              'Your card number:\n' + card_number + '\n'
              'Your card PIN:\n' + pin + '\n')
    else:
        print('Card already exist\n')


def login():
    user_card = input('\nEnter your card number:\n')
    user_pin = input('Enter your PIN:\n')
    if user_card in cards and user_pin == cards[user_card]:
        print('\nYou have successfully logged in!\n')
        return {'state': 'logged', 'id': user_card}
    print('\nWrong card number or PIN!\n')
    return {'state': 'main', 'id': 0}


cards = {}
balance = {}
cmd = ''
current = {'state': 'main', 'id': 0}
menu = {'main': '1. Create an account\n2. Log into account\n0. Exit\n',
        'logged': '1. Balance\n2. Log out\n0. Exit\n'}
while cmd != '0':
    print(cards)
    cmd = input(menu[current['state']])
    if current['state'] == 'main':
        if cmd == '1':
            create_account()
        elif cmd == '2':
            current = login()
    elif current['state'] == 'logged':
        if cmd == '1':
            print('\nBalance:', balance[current['id']], '\n')
        elif cmd == '2':
            print('\nYou have successfully logged out!\n')
            current['state'] = 'main'
