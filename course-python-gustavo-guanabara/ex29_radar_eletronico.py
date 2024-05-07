# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velC = float(input('Qual a velocidade atual do carro? '))
taxa = (velC - 80) * 7.00
if velC > 80:
    print(f'MULTADO! Você excedeu o limite de velocidade e terá que pagar uma multa de R${taxa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')