# ======= Exercício =======
# 1. Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão
print("""
======= Operações Básicas =======
- Realiza e retorna o resultado das quatro operações básicas.
- Aceita somente duas entradas.
""")

number1 = int(input('Informe o primeiro número: '))
number2 = int(input('Informe o segundo número: '))

print(f'\n======= Resultado das Operações =======\n')

print(f'Soma: {number1 + number2}')
print(f'Subtração: {number1 - number2}')
print(f'Multiplicação: {number1 * number2}')
print(f'Divisão: {number1 / number2}')
