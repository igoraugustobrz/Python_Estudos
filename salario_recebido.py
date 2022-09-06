# Exercício - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

ganhoPorHora = float(input("Digite o seu ganho por hora: "))
horasTrabalhadas = float(input("Digite o total de horas trabalhadas no mês: "))

totalSalario = ganhoPorHora * horasTrabalhadas

print("O seu salário mensal é de R$", totalSalario)