water = int(input('Write how many ml of water the coffee machine has: '))
milk = int(input('Write how many ml of milk the coffee machine has: '))
beans = int(input('Write how many grams of coffee beans the coffee machine has: '))
cups = int(input('Write how many cups of coffee you will need: '))
cups_possible = min(water // 200, milk // 50, beans // 15)
if cups_possible > cups:
    print('Yes, I can make that amount of coffee (and even',
          cups_possible - cups, 'more than that)')
elif cups_possible == cups:
    print('Yes, I can make that amount of coffee')
else:
    print('No, I can make only', cups_possible, 'cups of coffee')
