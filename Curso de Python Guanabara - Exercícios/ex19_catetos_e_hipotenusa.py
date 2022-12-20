# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa
cO = float(input("Comprimento do cateto oposto: "))
cA = float(input("Comprimento do cateto adjacente: "))
hip = (cO ** 2 + cA ** 2) ** 0.5
print(f'O comprimento da hipotenusa é {hip}')