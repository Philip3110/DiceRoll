import random

firstdice = 0  # set the value to 0
secdic = 0

game_run = True
print('Welcome do the roll dice game!')

while game_run:
    game = input('Do you wanna roll a dice? type y/n')
    if game[0] == 'y':  # checking if the input is 'yes or y'
        game_run = True
        firstdice = random.randint(1, 6)  # get a random nuber
        secdic = random.randint(1, 6)
        print('The number on first dice is: ' + str(firstdice))
        print('The number on Seconf dice is: ' + str(secdic))

        # add the two dices and get a total
        print('The total of all the dices is: '+str(firstdice + secdic))
    else:
        print('Thank you for rolling the dice')
        game_run = False
