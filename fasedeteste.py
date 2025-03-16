import random as r
import time as t
from randomize_dices import roll_animation as roll
from randomize_dices import dice_one, dice_two, dice_three, dice_four, dice_five, dice_six


# lógica

def getDice(bet):
    global balance
    dice_result = r.randint(1, 6)
    dices = [dice_one, dice_two,dice_three, dice_four, dice_five, dice_six]
    result = roll()

    if bet == dice_result:
        balance += bet_value
        result[0]()
        dices[dice_result-1]()
        print(f'Você venceu! Sua aposta: {bet} | Resultado: {dice_result}')
        print('')
        print(f'Seu saldo: {balance}')


    else:
        balance -= bet_value
        result[0]()
        dices[dice_result-1]()
        print(f'Você perdeu! Sua aposta: {bet} | Resultado: {dice_result}')
        print('')
        print(f'Seu saldo: {balance}')





# interface

print(' Bozó Online ')
print(' ----------- ')
print('')
print(f' Seu saldo: R$ 100.0 ')
print(' O que quer fazer? ')
print('')
print(' Digite "1" para: Participar da mesa ')
print(' Digite "2" para: Sair do jogo ')
print('')
while True:
    entrace = input('')
    if entrace == '1':
        print(f'Você sentou na mesa {r.randint(1, 1500)}')
        balance = 100.0
        #print(f'Digite "EXIT" para sair da mesa a qualquer momento.')  | Ainda não implementado
        while entrace == '1':
            bet_value = float(input('Quanto você quer apostar? '))
            if bet_value <= 0 or bet_value > balance:
                print('')
                print('Impossivel apostar esse valor')
                print('')
            elif bet_value == 'EXIT'.upper(): # | Ainda não implementado
                entrace = 'EXIT'
            else:
                print('')
                print(f'R$ {bet_value} apostado! | Seu saldo atual: R$ {balance - bet_value}')
                print('')
                bet = int(input('De 1 a 6, em qual número o dado parará? '))
                print('')
                if bet <= 0 or bet > 6:
                    print('')
                    print('Escolha um número somente de 1 a 6')
                    print('')
                else:
                    getDice(bet)
    elif entrace == 'EXIT'.lower():
        break













    elif entrace == '2':
        print('2')
    else:
        print('Nenhuma opção correspondente. ')






