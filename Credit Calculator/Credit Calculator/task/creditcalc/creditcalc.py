principal = int(input('Enter the credit principal: '))
what_to_calculate = input('''What do you want to calculate? 
    type "m" - for count of months, 
    type "p" - for monthly payment: ''')
if what_to_calculate == 'm':
    monthly_payment = int(input('Enter monthly payment: '))
    month = principal // monthly_payment
    if month * monthly_payment < principal:
        month += 1
    s = ''
    if month != 1:
        s = 's'
    print()
    print('It takes ' + str(month) + ' month' + s + ' to repay the credit')
elif what_to_calculate == 'p':
    month = int(input('Enter count of months: '))
    print()
    if principal % month == 0:
        print('Your monthly payment = ' + str(principal // month))
    else:
        payment = round(principal / month) + 1
        print('Your monthly payment = ' + str(payment)
              + ' with last month payment = ' + str(principal - (month - 1) * payment) + '.')
