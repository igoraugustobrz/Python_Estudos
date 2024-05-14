# ======= Exercício =======
# 1. Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz.
import numpy as np

print(f'\n======= Soma de Matrizes =======\n')

matriz = np.array([[3, 4, 1],
                  [3, 1, 5]])
addition = 0

for i in range(matriz.shape[0]):
  for j in range(matriz.shape[1]):
    addition += matriz[i][j]
print(f'Soma da Matriz: {addition}')