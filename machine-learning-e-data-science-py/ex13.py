# ======= Exercício =======
# 1. Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
# - ValueError: se o usuário digitar um caracter
# - ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
# - IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
# - KeyboardInterrupt: caso o usuário interrompa a execução

print(f'======= Tratamento de Exceções =======\n')

numbers = []

while True:
  try:
    numbers.append(float(input('Digite o 1º número: ')))
    numbers.append(float(input('Digite o 2º número: ')))
    
    division = numbers[0] / numbers[1]    
    break
  except ValueError:
    print('Valor digitado incompátivel. Tente novamente!')
  except ZeroDivisionError:
    print('Não é possível dividir um número por zero. Tente novamente!')
  except KeyboardInterrupt:
    print('\n\nUsuário interrompeu a execução do programa')
    break
  else:
    print(f'\nResultado da divisão: {division}')
