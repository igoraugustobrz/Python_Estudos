# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Qual o ano você quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O {ano} é BISSEXTO!')
else:
    print(f'{ano} não é um ano bissexto!')
