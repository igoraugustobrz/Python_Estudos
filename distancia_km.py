# Entrada de Dados
distanciaKm = int(input("Informe a distância a ser percorrida: "))

# Processamento e Saída de Dados
if distanciaKm <= 200:
    print("O preço da passagem ficou em R$", distanciaKm * 0.50)
    
else:
    print("O preço da passagem ficou em R$", distanciaKm * 0.45)