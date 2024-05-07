# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal
# – 3x ou mais no cartão: 20% de juros
print('=-' * 5, 'LOJAS AUGUSTO', '=-' * 5)
preco = float(input('Preço das compras R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão
''')
opcaoPg = int(input('Qual a forma de pagamento? '))

if opcaoPg == 1:
    total = preco - (preco * 10 / 100)
    print(f'Sua compra de R${preco:.2f} à vista dinheiro/cheque vai custar R${total:.2f}')

elif opcaoPg == 2:
    total = preco - (preco * 5 / 100)
    print(f'Sua compra de R${preco:.2f} à vista no cartão vai custar R${total:.2f}')

elif opcaoPg == 3:
    print(f'Sua compra de R${preco:.2f} em até 2x no cartão vai custar R${preco}')

elif opcaoPg == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = preco * 20 / 100
    aplcJuros = preco + juros
    pl = aplcJuros/parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${pl:.2f} COM JUROS')
    print(f'Sua compra de R${preco} vai custar R${aplcJuros:.2f} no final.')

else:
    print('\033[31mOpção inválida. Tente novamente!\033[m')
