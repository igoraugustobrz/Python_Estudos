# ======= Exercício =======
# 1. Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados.
print('======= Listas =======\n')

numbers = []
addition = 0

for i in range(1, 6):
  number = int(input(f'Digite o {i}º número: '))
  numbers.append(number)

for element in numbers:
  addition += element
  
print(f'\n======= Lista =======\nSoma dos elementos: {addition}')