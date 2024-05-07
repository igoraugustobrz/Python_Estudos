# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
from time import sleep
print("\033[33m============ DESAFIO 2 ==============\033[m")
dia = int(input("Qual o dia de nascimento? "))
mes = int(input("Qual o mês de nascimento? "))
ano = int(input("Qual o ano de nascimento? "))
print('Processando...')
sleep(0.8)
print(f"Você nasceu nesta data: \033[36m{dia}\033[m/\033[34m{mes}\033[m/\033[33m{ano}\033[m")