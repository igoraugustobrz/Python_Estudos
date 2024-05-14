# ======= Exercício =======
# 1. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
# - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
# - Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
# - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

print(f'======= Conversão de ºC para ºF =======\n')

def readTemperature():
  celsius = int(input('Informe a temperatura em ºC: '))
  return celsius

def convertFahrenheit(c):
  fahrenheit = (9 * c + 160) / 5
  return fahrenheit

def displayResult(f):
  print(f'\nAgora fazem {f} ºF')
  
celsius = readTemperature() 
fahrenheit = convertFahrenheit(celsius)
displayResult(fahrenheit)