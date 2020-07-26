first_num = float(input())
second_num = float(input())
oper = input()


def calculator(first, second, operation):
    if operation in ('/', 'mod', 'div') and second == 0:
        print('Division by 0!')
    elif operation == '+':
        print(first + second)
    elif operation == '-':
        print(first - second)
    elif operation == '/':
        print(first / second)
    elif operation == '*':
        print(first * second)
    elif operation == 'mod':
        print(first % second)
    elif operation == 'pow':
        print(first ** second)
    elif operation == 'div':
        print(first // second)


calculator(first_num, second_num, oper)
