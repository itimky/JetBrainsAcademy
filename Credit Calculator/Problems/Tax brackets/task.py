income = int(input())
if income >= 132407:
    percent = 28
elif income >= 42708:
    percent = 25
elif income >= 15528:
    percent = 15
else:
    percent = 0
calculated_tax = round(income * percent / 100)
print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')