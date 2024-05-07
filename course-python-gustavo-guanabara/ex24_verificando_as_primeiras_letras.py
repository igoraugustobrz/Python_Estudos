# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.
cid = str(input('Informe o nome da cidade: ')).lower().split()
print(f'O nome da cidade começa com Santo? ', end='')
print('santo' in cid[0])
