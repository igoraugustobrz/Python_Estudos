# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0:  # Computador jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')

    elif jogador == 2:
        print('COMPUTADOR VENCE')

    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:  # Computador jogou Papel
    if jogador == 0:  # Jogador jogou Pedra
        print('COMPUTADOR VENCE')

    elif jogador == 1: # Jogador jogou Papel
        print('EMPATE')

    elif jogador == 2: # Jogador jogou Tesoura
        print('JOGADOR VENCE')

elif computador == 2:  # Computador jogou Tesoura
    if jogador == 0: # Jogador jogou Pedra
        print('JOGADOR VENCE')

    elif jogador == 1: # Jogador jogou Papel
        print('COMPUTADOR VENCE')

    elif jogador == 2: # Jogador jogou Tesoura
        print('EMPATE')
