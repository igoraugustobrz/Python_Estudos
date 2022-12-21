# Crie um programa que mostre na tela todos os números pares entre 1 e 50.
from time import sleep
print('-=' * 9)
print('PARES ENTRE 1 E 50')
print('-=' * 9)
for numeros in range(1, 51):
    if numeros % 2 == 0:
        print(numeros)
        sleep(0.2)
