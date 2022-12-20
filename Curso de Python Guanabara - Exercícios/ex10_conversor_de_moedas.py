# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere U$1.00 = R$3.27

carteira = float(input("Digite a quantidade de dinheiro que você tem na carteira R$"))
print(f"Com o dinheiro informado é possível comprar US${round(carteira/3.27, 2)} dólar/dólares")
