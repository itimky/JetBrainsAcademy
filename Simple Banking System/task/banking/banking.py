import random


def luhn(card_without_checksum):
    checksum = 0
    for order, n in enumerate(card_without_checksum):
        check = int(n) * ((order + 1) % 2 + 1)
        checksum += check if check <= 9 else check - 9
    checksum = 10 - checksum % 10
    return '0' if checksum == 10 else str(checksum)


def create_account():
    bank_id = '400000'
    acc_id = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    checksum = luhn(bank_id + acc_id)
    card_number = bank_id + acc_id + checksum
    pin = ''.join([str(random.randint(0, 9)) for _ in range(4)])
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


qwe = ''.join([str(random.randint(0, 9)) for _ in range(9)])
print(qwe)


cards = {}
balance = {}
cmd = ''
current = {'state': 'main', 'id': 0}
menu = {'main': '1. Create an account\n2. Log into account\n0. Exit\n',
        'logged': '1. Balance\n2. Log out\n0. Exit\n'}
while cmd != '0':
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
