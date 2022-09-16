# Exercício - Faça um programa que pergunte ao usuário o valor que ele tem investido e a taxa percentual
# que ele ganha ao mês (juros simples). Calcule e imprima o total ganho com o investimento em 3 meses

valorInvestido = int(input("Digite o valor investido: "))
taxaDeJuros = int(input("Informe o percentual de juros simples por mês: "))

taxaDeJuros = taxaDeJuros/100
formulaJurosSimples = valorInvestido * taxaDeJuros * 3

print("O total ganho com o investimento em 3 meses é de ", formulaJurosSimples)
