# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = float(input('Qual a distância da sua viagem? '))
if dist <= 200:
    print(f'Com uma taxa de R$0.50 para viagens curtas, o total a ser pago ficou em R${dist * 0.50:.2f}')
else:
    print(f'Com uma taxa de R$0.45 para viagens longas, o total a ser pago ficou em R${dist * 0.45:.2f} ')

    # Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
    # Km para viagens de até 200Km e R$0,45 parta viagens mais longas.