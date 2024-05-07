# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2.

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
lTinta = area/2
print(f"Sua parede tem a dimensão {largura}x{altura} e sua área é de {round(area, 2)}m². ", end='')
print(f"Para pintar essa parede, você precisará de {round(lTinta, 2)}l tinta.")