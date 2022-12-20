# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo
# será negado.
casa = float(input('Valor da Casa: R$'))
salario = float(input('Salário do Comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))
prestMensal = casa / (tempo * 12)
porc30 = (salario * 30) / 100
print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos a prestação será de R${prestMensal:.2f}')
if prestMensal > porc30:
    print('\033[0;31mEmpréstimo NEGADO!')
else:
    print('\033[0;32mEmpréstimo APROVADO!')