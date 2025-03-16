from time import sleep
import random as r


# design

def dice_one():
    print('   ____________')
    print('  /          / |')
    print(' /          /  |')
    print('/----------/   |')
    print('|          |   /')
    print('|    •     |  /')
    print('|          | /')
    print('|__________|/')
    sleep(0.4)
    print('')
    sleep(0.0)

def dice_two():
    print('   ____________')
    print('  /          / |')
    print(' /          /  |')
    print('/----------/   |')
    print('|        • |   /')
    print('|          |  /')
    print('| •        | /')
    print('|__________|/')
    sleep(0.4)
    print('')
    sleep(0.0)

def dice_three():
    print('   ____________')
    print('  /          / |')
    print(' /          /  |')
    print('/----------/   |')
    print('|        • |   /')
    print('|    •     |  /')
    print('| •        | /')
    print('|__________|/')
    sleep(0.4)
    print('')
    sleep(0.0)

def dice_four():
    print('   ____________')
    print('  /          / |')
    print(' /          /  |')
    print('/----------/   |')
    print('| •      • |   /')
    print('|          |  /')
    print('| •      • | /')
    print('|__________|/')
    sleep(0.4)
    print('')
    sleep(0.0)

def dice_five():
    print('   ____________')
    print('  /          / |')
    print(' /          /  |')
    print('/----------/   |')
    print('| •      • |   /')
    print('|    •     |  /')
    print('| •      • | /')
    print('|__________|/')
    sleep(0.4)
    print('')
    sleep(0.0)

def dice_six():
    print('   ____________')
    print('  /          / |')
    print(' /          /  |')
    print('/----------/   |')
    print('| •      • |   /')
    print('| •      • |  /')
    print('| •      • | /')
    print('|__________|/')
    sleep(0.4)
    print('')
    sleep(0.0)

# logicmb nv

def roll_animation():
    random_dice = (dice_one, dice_two, dice_three, dice_four, dice_five, dice_six)
    for dice in random_dice:
        dice = r.randrange(len(random_dice))
        random_dice[dice]()

    return [random_dice[dice], dice]


