# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
opUser = int(input('Qual é a sua jogada? '))
string = 'Pedra Papel Tesoura'
opcoes = string.split()
opComp = randint(0, 2)
print(f'''Jogador jogou {opcoes[opUser]}
Computador jogou {opcoes[opComp]}''')

if opComp == 0 and opUser == 2:
    print('Jogador PERDEU')
else:
    if opComp == 2 and opUser == 0:
        print('Jogador VENCEU')
    else:
        pass

if opComp == 1 and opUser == 0:
    print('Jogador PERDEU')
else:
    if opComp == 0 and opUser == 1:
        print('Jogador VENCEU')

if opUser == opComp:
    print('EMPATE')