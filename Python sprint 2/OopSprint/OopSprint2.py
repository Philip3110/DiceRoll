import random


class dice:  # class created
    num = 0

    def roll():
        num = random.randint(1, 6)  # get random number
        return num


game_run = True
print('Welcome to this fun rolling game!')

while game_run:
    game = input('Do you wanna roll a dice? type y/n')
    if game[0] == 'y':  # check if player wants to play by checking the input
        d1 = dice
        d2 = dice

        num1 = d1.roll()  # make a roll of the dice
        num2 = d2.roll()
        print(str(num1))  # get the value of num1
        print(str(num2))
        print('Total of both dices is:' + str(num1 + num2))
    else:
        print('Thank you for rolling the dice')
        game_run = False
