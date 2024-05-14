# ======= Exercício =======
#1. Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
# - Função para ler os valores (não recebe parâmetro e retorna os dois valores)
# - Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
# - Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
# - Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)

print(f'======= Cálculo de Combustível Utilizado (com funções) =======\n')

def readValues():
  t = float(input("Informe o tempo gasto na viagem: "))
  avg = float(input("Informe a velocidade média: "))
  return t, avg

def calculateDistance(time, velocity):
  d = time * velocity
  return d

def usedLiters(d):
  liters = d / 12
  return liters

def displayResult(vel, time, distan, liter):
  print(f'\n======= Resultados =======\n')
  print(f'Velocidade Média: {vel}')
  print(f'Tempo gasto: {time}')
  print(f'Distância Percorrida: {distan}')
  print(f'Litros usados: {liter}')


timeSpent, velocity = readValues()

calculateDistance(timeSpent, velocity)
distance = calculateDistance(timeSpent, velocity)

usedLiters(distance)
liters = usedLiters(distance)

displayResult(velocity, timeSpent, distance, liters)

