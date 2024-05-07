# Faça um programa que leia um número inteiro e mostre na tela a sua tabuada.
numero = int(input("Tabuada do: "))
contador = 0
tabuada = 0
    
while contador <= 10:
   print(f'{numero} * {contador} = {numero * contador}')
   contador = contador + 1