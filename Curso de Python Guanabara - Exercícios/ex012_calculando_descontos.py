# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
precoP = float(input("Qual o preço do produto? R$"))
desc5 = (5 * precoP)/100
print(f"O produto que custava R${precoP}, com 5% de desconto agora custa R${round(precoP - desc5, 2)}" )