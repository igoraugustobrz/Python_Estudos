# Exercício - Crie um programa que recebe como entrada dois números inteiros, divida o primeiro número
# pelo segundo e imprima na tela, separadamente, a parte inteira da divisão e o resto.

dividendo = int(input("Digite o valor do dividendo: "))
divisor  = int(input("Digite o valor do divisor: "))

divisao = dividendo/divisor
resto = dividendo % divisor

print("O resultado da divisão é: ", divisao, "e o resto é: ", resto )
