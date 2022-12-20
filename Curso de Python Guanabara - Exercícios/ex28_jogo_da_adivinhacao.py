# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randrange
from time import sleep
GREEN = "\033[0;32m"
RED = "\033[1;31m"
print('-=' * 28)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 28)
nJog = int(input('Em que número eu pensei? '))
nComp = randrange(0, 5)
print(RED + 'PROCESSANDO...')
sleep(3)
if nJog == nComp:
    print(GREEN + 'PARABÉNS ! Você conseguiu me vencer!')
else:
    print(GREEN + f'GANHEI ! Eu pensei no número {nComp} e não no {nJog}!')