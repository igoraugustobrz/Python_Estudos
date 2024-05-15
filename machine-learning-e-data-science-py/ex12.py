# ======= Exercício =======
# 1. Crie um arquivo .py com duas funções
# - Função para ler um string (recebe como parâmetro uma mensagem e retorna o que o usuário digitou)
# - Função para ler um número float (recebe como parâmetro uma mensagem e retorna o que o usuário digitou)

def readString(message):
  return input(message)
  
def readNumber(number):
  return float(input(number))

name = readString('Digite seu nome: ')
print(name)

num = readNumber('Digite um número: ')
print(num)