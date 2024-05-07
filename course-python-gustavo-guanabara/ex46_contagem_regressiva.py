# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0.
# Com um pausa de 1 segundo entre eles.
from time import sleep
print('-=' * 15)
print('ESTOURO DE FOGOS DE ARTIFÍCIO')
print('-=' * 15)
print(' ' * 15)
for contagem in range(10, 0, -1):
    print(contagem)
    sleep(1)
print('🎆🎆🎆')
