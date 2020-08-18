import random
import sqlite3
import string


def luhn(card_without_checksum):
    checksum = 0
    for order, n in enumerate(card_without_checksum):
        check = int(n) * ((order + 1) % 2 + 1)
        checksum += check if check <= 9 else check - 9
    checksum = 10 - checksum % 10
    return '0' if checksum == 10 else str(checksum)


def create_account(connection):
    bank_id = '400000'
    acc_id = ''.join(random.sample(string.digits, 9))
    checksum = luhn(bank_id + acc_id)
    card_number = bank_id + acc_id + checksum
    pin = ''.join(random.sample(string.digits, 4))
    cursor = connection.cursor()
    cursor.execute('SELECT number FROM card')
    if (card_number,) not in cursor.fetchall():
        cursor.execute(f"INSERT INTO card (number, pin) VALUES ('{card_number}', '{pin}')")
        connection.commit()
        print('\nYour card has been created\n'
              'Your card number:\n' + card_number + '\n'
              'Your card PIN:\n' + pin + '\n')
    else:
        print('Card already exist\n')
    cursor.close()
    return None


def login(connection):
    user_card = input('\nEnter your card number:\n')
    user_pin = input('Enter your PIN:\n')
    if user_card.isdigit() and user_pin.isdigit():
        cursor = connection.cursor()
        cursor.execute(f"SELECT id, number, pin FROM card WHERE number = '{user_card}'")
        data = cursor.fetchone()
        cursor.close()
        if data:
            db_id, db_card, db_pin = data
            if db_pin == user_pin:
                print('\nYou have successfully logged in!\n')
                return {'state': 'logged', 'id': db_id}
    print('\nWrong card number or PIN!\n')
    return {'state': 'main', 'id': 0}


def get_balance(connection, current):
    cursor = connection.cursor()
    cursor.execute(f'SELECT balance FROM card WHERE id = {current["id"]}')
    balance = cursor.fetchone()[0]
    return balance


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS card ('
                   'id INTEGER PRIMARY KEY, '
                   'number TEXT, '
                   'pin TEXT, '
                   'balance INTEGER DEFAULT 0)'
                   ';')
    connection.commit()
    cursor.close()
    return None


def add_income(connection, current):
    income = int(input('\nEnter income:\n'))
    cursor = connection.cursor()
    cursor.execute(f'UPDATE card SET balance = balance + {income} WHERE id = {current["id"]}')
    connection.commit()
    print('Income was added!\n')
    cursor.close()
    return None


# def print_card(connection):
#     cursor = connection.cursor()
#     cursor.execute('SELECT number FROM card')
#     print(cursor.fetchall())
#     cursor.close()


conn = sqlite3.connect('card.s3db')
create_table(conn)
cmd = ''
curr = {'state': 'main', 'id': 0}
menu = {'main': '1. Create an account\n'
                '2. Log into account\n'
                '0. Exit\n',
        'logged': '1. Balance\n'
                  '2. Add income\n'
                  '3. Do transfer\n'
                  '4. Close account\n'
                  '5. Log out\n'
                  '0. Exit\n'}
while cmd != '0':
    cmd = input(menu[curr['state']])
    if curr['state'] == 'main':
        if cmd == '1':
            create_account(conn)
        elif cmd == '2':
            curr = login(conn)
        # elif cmd == '3':
        #     print_card(conn)
    elif curr['state'] == 'logged':
        if cmd == '1':
            print('\nBalance:', get_balance(conn, curr), '\n')
        elif cmd == '2':
            add_income(conn, curr)
        elif cmd == '3':
            pass
        elif cmd == '4':
            pass
        elif cmd == '5':
            print('\nYou have successfully logged out!\n')
            curr = {'state': 'main', 'id': 0}
conn.close()
