class CoffeeMachine:
    def __init__(self):
        self.res = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}
        self.state = 'choosing an action'

    def __str__(self):
        return ('\nThe coffee machine has:\n' +
                str(self.res['water']) + ' of water\n' +
                str(self.res['milk']) + ' of milk\n' +
                str(self.res['beans']) + ' of coffee beans\n' +
                str(self.res['cups']) + ' of disposable cups\n$' +
                str(self.res['money']) + ' of money\n')

    def send(self, command):
        if self.state == 'choosing an action':
            if command == 'remaining':
                print(self)
                return None
            elif command == 'buy':
                print()
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ', end='')
                self.state = 'choosing coffee'
                return None
            elif command == 'fill':
                return self.fill()
            elif command == 'take':
                return self.take()
            else:
                return None
        elif self.state == 'choosing coffee':
            return self.buy(command)

    def buy(self, command):
        self.state = 'choosing an action'
        print()
        if command == '1':
            need = {'water': 250, 'milk': 0, 'beans': 16, 'cups': 1, 'money': -4}
        elif command == '2':
            need = {'water': 350, 'milk': 75, 'beans': 20, 'cups': 1, 'money': -7}
        elif command == '3':
            need = {'water': 200, 'milk': 100, 'beans': 12, 'cups': 1, 'money': -6}
        elif command == 'back':
            return None
        else:
            return None
        return self.make_coffee(need)

    def fill(self):
        print()
        water = int(input('Write how many ml of water do you want to add: '))
        milk = int(input('Write how many ml of milk do you want to add: '))
        beans = int(input('Write how many grams of coffee beans do you want to add: '))
        cups = int(input('Write how many disposable cups of coffee do you want to add: '))
        self.res['water'] += water
        self.res['milk'] += milk
        self.res['beans'] += beans
        self.res['cups'] += cups
        print()
        return None

    def take(self):
        print()
        print('I gave you $' + str(self.res['money']))
        print()
        self.res['money'] = 0
        return None

    def check_resources(self, need):
        out_of = []
        for item in self.res:
            if self.res[item] < need[item] and item != 'money':
                out_of.append(item)
        return out_of

    def resource_update(self, need):
        for item in self.res:
            self.res[item] -= need[item]
        return None

    def make_coffee(self, need):
        not_enough = self.check_resources(need)
        if not_enough:
            print('Sorry, not enough', *not_enough)
            print()
            return None
        else:
            print('I have enough resources, making you a coffee!')
            print()
            self.resource_update(need)
            return None


coffee_machine = CoffeeMachine()
c = ''
while c != 'exit':
    if coffee_machine.state == 'choosing an action':
        print('Write action (buy, fill, take, remaining, exit):', end='')
    c = input()
    coffee_machine.send(c)
