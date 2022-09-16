# Exercício - Construa um programa que receba o tamanho dos catetos de um triângulo retângulo e
# compute sua hipotenusa. Imprima o valor da hipotenusa na tela.

catetoAdjacente = int(input("Digite o valor do cateto adjacente: "))
catetoOposto = int(input("Digite o valor do cateto oposto: "))

hipotenusa = catetoAdjacente**2 + catetoOposto**2
calculoRaizHipotenusa = hipotenusa** 0.5

print("O resultado do cáluco da hipotenusa é: ", calculoRaizHipotenusa)