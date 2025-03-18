import random as r

print('Welcome to DICES')
print('    --- * ---')
print(' ')

def call_diceOne():
    dice_one = 1
    print('|---------|')
    print('|         |')
    print('|    •    |')
    print('|         |')
    print('|---------|')
    return dice_one

def call_diceTwo():
    dice_two = 2
    print('|---------|')
    print('|       • |')
    print('|         |')
    print('| •       |')
    print('|---------|')
    return dice_two

def call_diceThree():
    dice_three = 3
    print('|---------|')
    print('|       • |')
    print('|    •    |')
    print('| •       |')
    print('|---------|')
    return dice_three

def call_diceFour():
    dice_four = 4
    print('|---------|')
    print('| •     • |')
    print('|         |')
    print('| •     • |')
    print('|---------|')
    return dice_four

def call_diceFive():
    dice_five = 5
    print('|---------|')
    print('| •     • |')
    print('|    •    |')
    print('| •     • |')
    print('|---------|')
    return dice_five

def call_diceSix():
    dice_six = 6
    print('|---------|')
    print('| •     • |')
    print('| •     • |')
    print('| •     • |')
    print('|---------|')
    return dice_six

#por falta de ideia melhor, no momento

calling_dices = [call_diceOne(), call_diceTwo(), call_diceThree(), call_diceFour(), call_diceFive(), call_diceSix()]

r_num = r.randint(0, 5)
r_num_2 = r.randint(0, 5)

calling_random_dices_1 = [calling_dices[r_num], calling_dices[r_num_2]]

r_num_3 = r.randint(0, 5)
r_num_4 = r.randint(0, 5)

calling_random_dices_2 = [calling_dices[r_num_3], calling_dices[r_num_4]]


first_round = 0
if calling_random_dices_1[0] == 1 :
    first_round += call_diceOne()
if calling_random_dices_1[1] == 1:
    first_round +=call_diceOne()






while True:
    dice_choice = input('Os últimos dados vão ser maiores ">" ou menores "<" quer os primeiros? ')
    if dice_choice == '<':
        print('Certo, vamos ver o resultado.')
        print('')

    elif dice_choice == '>':
        print('b')
    else:
        print('n')