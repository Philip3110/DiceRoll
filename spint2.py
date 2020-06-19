import random

firstdice = 0  # set the value to 0
secdic = 0


def randomdice(firstdice, secdic):
    game_run = True
    firstdice = random.randint(1, 6)  # get a random number
    secdic = random.randint(1, 6)
    print('The number on first dice is: ' + str(firstdice))
    print('The number on Seconf dice is: ' + str(secdic))
    # Gets the sum of the 2 dices and add the 2 strings in a tuple
    totTuple = ('Total: ', str(firstdice + secdic))
    # Joins all the strings in the tuple into var 'total'
    total = ''.join(totTuple)
    print(total)


game_run = True
print('Welcome do the roll dice game!')

while game_run:
    game = input('Do you wanna roll a dice? type y/n')
    if game[0] == 'y':  # checking if the input is 'yes or y'
        randomdice(firstdice, secdic)

    elif game[0].lower() == 'n':
        print('Thank you for playing, come back soon.')
        game_run = False
    else:
        print('Pls type a y or a n and not any other letter or number.')
