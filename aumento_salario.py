# Entrada de dados
salario = float(input("Digite o seu salário: "))
aumento = int(input("Digite um aumento para o seu salário: "))

# Processamento
formulaAumento = aumento/100

# Saída
print("O seu novo salário ficou em:", (salario*formulaAumento)+salario)