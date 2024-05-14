# ======= Exercício =======
# 1. Ler 5 notas e informar a média
print('======= Cálculo da Média - While =======\n')

avg = 0

for note in range(1, 6):
  notes = int(input(f'Digite a {note}º nota: '))
  avg += notes
print(f'\nA média é {avg / 5}')