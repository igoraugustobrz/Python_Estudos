# Exercício 1 -Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

ladoA = int(input("Informe o valor do lado A: "))
ladoB = int(input("Informe o valor do lado B: "))
ladoC = int(input("Informe o valor do lado C: "))

if (ladoA + ladoB) >= ladoC:
    print("É um triângulo")
else:
    print("Não é um triângulo")

if (ladoA == ladoB) and (ladoC == ladoA) and (ladoC == ladoA):
    print("É do tipo Equilátero")

if (ladoA == ladoB) and (ladoC != ladoB):
    print("É do tipo Isóceles")

if (ladoA != ladoB) and (ladoB != ladoC):
    print("É tipo Escaleno")
