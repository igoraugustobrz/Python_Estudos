# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 a 500.
s = 0
for numeros in range(1, 501):
    if numeros % 2 != 0 and numeros // 3:
        print(numeros)
        s += numeros
print(s)