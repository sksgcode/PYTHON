from Menu&Resources import MENU
from Menu&Resources import resources

moneylvl = 0

# SUBROUTINES //////////////////////////////////////////////////////////////////////////////

# DEDUCTING RESOURCES

def makedrink(drinkname, ingredients):

    for item in ingredients:

        resources[item] -= ingredients[item]

    print(f'Here is your {drinkname}, Enjoy!')

# CHECKING TRANSACTION STATUS

def transaction(moneyin,drinkcost):

    if moneyin >= drinkcost:

        change = round(moneyin - drinkcost, 3)
        print(f'Here is ${change} in change.')

        global moneylvl
        moneylvl += drinkcost

        return True
    
    else:

        print('Sorry, that is not enough money. All cash refunded.')

        return False

# RECIEVING COINS

def coins():
    
    total = (int(input('Quarters: ')))*0.25
    total += (int(input('Dimes: ')))*0.10
    total += (int(input('Nickel: ')))*0.05
    total += (int(input('Pennies: ')))*0.01

    return total

# CHECK IF RESOURCES ARE AVALIABLE

def resourcecheck(ingredients):

    for item in ingredients:

        if ingredients[item] > resources[item]:

            print(f'Sorry, there is not enough {item}.')

            return False
        
    return True
    
# MAIN PROGRAM //////////////////////////////////////////////////////////////////////////////

loop = True

while loop:

    choice = input('What would you like? (espresso/latte/cappuccino): ')

    if choice == 'off':

        loop = False

    elif choice == 'report':

        print(f'Water: {resources["water"]}')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f'Money: {moneylvl}')
    
    else:

        drink = MENU[choice]

        if resourcecheck(drink['ingredients']):

            price = drink['cost']
            print(f'Please insert ${price} in coins.')

            moneyin = coins()

            if transaction(moneyin, drink['cost']):

                makedrink(choice, drink['ingredients'])

