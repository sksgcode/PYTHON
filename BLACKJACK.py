import random

# INTRODUCTION ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print('\n')
print('''WELCOME TO
▄▄▄▄· ▄▄▌   ▄▄▄·  ▄▄· ▄ •▄      ▐▄▄▄ ▄▄▄·  ▄▄· ▄ •▄ 
▐█ ▀█▪██•  ▐█ ▀█ ▐█ ▌▪█▌▄▌▪      ·██▐█ ▀█ ▐█ ▌▪█▌▄▌▪
▐█▀▀█▄██▪  ▄█▀▀█ ██ ▄▄▐▀▀▄·    ▪▄ ██▄█▀▀█ ██ ▄▄▐▀▀▄·
██▄▪▐█▐█▌▐▌▐█ ▪▐▌▐███▌▐█.█▌    ▐▌▐█▌▐█ ▪▐▌▐███▌▐█.█▌
·▀▀▀▀ .▀▀▀  ▀  ▀ ·▀▀▀ ·▀  ▀     ▀▀▀• ▀  ▀ ·▀▀▀ ·▀  ▀\n''')

# GLOBAL VALUES /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

endgame = False

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

lost = 'BUST! You lose\n'
win = 'VICTORY! You win\n'

# FINAL FUNCTION /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def final():
    print(f'BTW, dealer got {npctotal}\n')
    again = input('Would you like to play again? Type Y or N: \n').upper()
    if again == 'N':
        endgame = True

# CHECKING FUNCTION /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def check(total,npctotal):
    if npctotal > 21:
        print(win)
        final()

    elif total > npctotal:
        print(win)
        final()

    elif total == npctotal:
        print('Its a DRAW!')
        final()
    
    elif total < npctotal:
        print(lost)
        final()

# CHOICE WHEN A /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def choice():
    choice = int(input('Choose between 1 and 11: \n'))
    return choice

# MAIN PROGRAM /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

while endgame == False:

# FIRST CARD SELECTION

    npccard1 = random.choice(cards)
    print(f"Dealer's first card is {npccard1}\n")
    usrcard1 = random.choice(cards)
    if usrcard1 == 11:
        usrcard1 = choice()

    print(f"Your first card is {usrcard1}\n")

# SECOND CARD SELECTION

    npccard2 = random.choice(cards)
    print("Dealer has chosen a hidden card\n")
    usrcard2 = random.choice(cards)
    if usrcard2 == 11:
        usrcard2 = choice()
    print(f"Your second card is {usrcard2}\n")

# RUNNING TOTALS

    npctotal = npccard1 + npccard2

    total = usrcard1 + usrcard2

# FIRST CHECK

    if total > 21:
        print(lost)

# THIRD CARD DECISION

    else:
        print(f'Your current total is {total}.\n')
        ans = input('would you like to choose another card? Type Y or N: \n').upper()

        # THIRD CARD CHOICE

        if ans == 'Y':

            usrcard3 = random.choice(cards)
            if usrcard3 == 11:
                usrcard3 = choice()

            print(f"Your third card is {usrcard3}\n")
            
            # CURRENT TOTAL

            total += usrcard3

            print(f'Your total is now {total}.\n')

            if total > 21:
                print(lost)
                final()

            else:
                check(total,npctotal)

        elif ans == 'N':

            check(total,npctotal)
        
        else:
            print('Invalid input.')