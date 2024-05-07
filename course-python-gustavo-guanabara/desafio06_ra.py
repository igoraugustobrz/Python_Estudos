# Criar um programa que pegue todos os caracteres de seu RA, transforme em números (baseado em sua posição no alfabeto),
# e apresente o resultado da soma.
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
soma = 0
ra = input('R.A: ').upper()
for x in ra:
    for posicao, letra in enumerate(alfabeto):
        if x == letra:
            soma += posicao + 1
print(soma)