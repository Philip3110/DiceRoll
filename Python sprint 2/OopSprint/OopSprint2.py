import random


class dice:
    num = 0

    def roll():
        num = random.randint(1, 6)
        return num


game_run = True

while game_run:
    game = input('Do you wanna roll a dice? type y/n')
    if game[0] == 'y':
        d1 = dice
        d2 = dice

        num1 = d1.roll()
        num2 = d2.roll()
        print(str(num1))
        print(str(num2))
        print('Total of both dices is:' + str(num1 + num2))
    else:
        print('Thank you for rolling the dice')
        game_run = False
