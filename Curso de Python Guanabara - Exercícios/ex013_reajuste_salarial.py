# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Qual é o seu salário? R$"))
novSal = (15 * salario)/100
print(f"Um funcionário que ganhava R${round(salario, 2)}, com 15% de aumento, passa a receber R${round(salario + novSal, 2)}")