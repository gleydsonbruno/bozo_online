import random as r
import time as t


# lógica

def getDice(x):
    dice_result = r.randint(1, 6)
    if x == dice_result:
        print(f'Você venceu! Sua aposta: {x} | Resultado: {dice_result}')
    else:
        print(f'Você perdeu! Sua aposta: {x} | Resultado: {dice_result}')


# interface

print(' Bozó Online ')
print(' ----------- ')
print('')
balance = 100.00
print(f' Seu saldo: R$ {balance} ')
print('O que quer fazer? ')
print(' Digite "1" para: Participar da mesa ')
print(' Digite "2" para: Sair do jogo ')
while True:
    entrace = input('')
    if entrace == '1':
        print('Você sentou em uma mesa.')
        bet = int(input('De 1 a 6, qual número o dado dará? '))
        if bet <= 0 or bet > 6:
            print('Escolha um número somente de 1 a 6')
        else:
            getDice(bet)

    elif entrace == '2':
        print('2')
    else:
        print('Nenhuma opção correspondente. ')






