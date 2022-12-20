# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas
# - Quantas letras ao todo (sem considerar os espaços).
# - Quantas letras tem o primeiro nome.
nC = input('Digite seu nome completo: ')
print(f'Com todas as letras maiúsculas seu nome fica: {nC.upper()}')
print(f'Com todas as letras minúsculas seu nome fica: {nC.lower()}')
frase = nC.split(' ')
nova = ''.join(frase)
print(f'Sem considerar os espaços, seu nome tem {len(nova)} letras')
print(f'O primeiro nome tem {len(frase[0])} letras')
