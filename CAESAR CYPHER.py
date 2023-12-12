alphabet = []

for i in range (97,123):

    alphabet += chr(i)

print (alphabet)

again = True

while again == True:

    choice = input('Do you want to encrypt [e] or decrypt [d] a message?: ').lower()


    if choice == 'e':

        word = input('What would you like to encrypt?: ').lower()
        shift = int(input('What shift key would you like to use?: '))
        wordlen = len(word)

        final = []

        for position in range (wordlen):

            letter = word[position]

            if letter in alphabet:

                income = ord(letter)
                outcome = income + shift

                if outcome >= 123:

                    outcome = 97 + (outcome - 123)

                answer = chr(outcome)

            else:

                answer = letter
            
            final += answer
        
        encrypted = ''.join(final)
        print(f'Your encrypted message is: {encrypted}')

        another = input('Would you like to run the program again, yes [y] or no [n]?: ').lower()

        if another == 'y':
            again = True
        else:
            again = False

    
    elif choice == 'd':

        word = input('What would you like to decrypt?: ').lower()
        shift = int(input('What shift key would you like to use?: '))
        wordlen = len(word)

        final = []

        for position in range (wordlen):

            letter = word[position]

            if letter in alphabet:

                income = ord(letter)
                outcome = income - shift
##################################### WORK ON THIS LATER #####################################
                if outcome < 97:

                    outcome += 26

                answer = chr(outcome)

            else:

                answer = letter
            
            final += answer

        encrypted = ''.join(final)
        print(f'Your encrypted message is {encrypted}')

        another = input('Would you like to run the program again, yes [y] or no [n]?: ').lower()

        if another == 'y':
            again = True
        else:
            again = False




        


