# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Funcionário (a), digite seu salário R$'))
if salario > 1250:
    aumento = (salario * 10) / 100
    print(f'O novo salário com aumento de 10% é R${salario + aumento:.2f}')
else:
    aumento = (salario * 15) / 100
    print(f'O novo salário com aumento de 15% é R${salario + aumento:.2f}')