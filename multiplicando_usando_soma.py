# Exerício - Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo.
# Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a
# multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4

primeiroFator = int(input("Digite o primeiro número: "))
segundoFator = int(input("Digite o segundo número: "))
contador = 1
produto = 0

while contador <= segundoFator:
    produto = produto + primeiroFator
    contador = contador + 1

print(primeiroFator, "x", segundoFator, " = ", produto)
    