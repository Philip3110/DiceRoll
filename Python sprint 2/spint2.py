import random

firstdice = 0
secdic = 0

game_run = True

while game_run:
    game = input('Do you wanna roll a dice? type y/n')
    if game[0] == 'y':
        game_run = True
        firstdice = random.randint(1, 6)
        secdic = random.randint(1, 6)
        print('The number on first dice is: ' + str(firstdice))
        print('The number on Seconf dice is: ' + str(secdic))

        print('The total of all the dices is: '+str(firstdice + secdic))
    else:
        print('Thank you for rolling the dice')
        game_run = False
