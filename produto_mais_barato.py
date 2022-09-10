# Exercício - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo
# que a decisão é sempre pelo mais barato.
mercadoria1 = float(input("Digite o preço da primeira mercadoria: "))
mercadoria2 = float(input("Digite o preço da segunda mercadoria: "))
mercadoria3 = float(input("Digite o preço da terceira mercadoria: "))

if mercadoria1 < mercadoria2 and mercadoria1 < mercadoria3:
    print("Recomendamos você comprar a primeira mercadoria!")

if mercadoria2 < mercadoria1 and mercadoria2 < mercadoria3:
    print("Recomendamos você comprar a segunda mercadoria!")

elif mercadoria3 < mercadoria1 and mercadoria3 < mercadoria2:
    print("Recomendamos você comprar a terceira mercadoria!")

