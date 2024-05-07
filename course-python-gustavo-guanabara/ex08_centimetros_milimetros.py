# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros
m = float(input('Digite uma distância em metros: '))
print(f'{m}m corresponde a {round(m * 100, 1)}cm e a {round(m * 1000, 1 )}mm.')