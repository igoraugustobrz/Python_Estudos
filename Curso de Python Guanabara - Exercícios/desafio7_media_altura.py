# Escreva um programa com uma lista chamada “altura”. Nesta lista, deve conter 8 alturas de pessoas
# diversas (ex: 1.80, 1.55, 1.74, 1.83, 1.60, 1.67, 1.79, 1.85). Calcule a média e mostre o resultado no
# interpretador.
altura = []
for x in range(0, 8):
    pdA = float(input(f'{x + 1}Altura: '))
    altura.append(pdA)
print(f'Média: {round(sum(altura)/len(altura))}')
