# ======= Exercício =======
# 1.Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média
print(f'\n======= Média dos alunos (dicionário) =======\n')

addition = 0
students = {}

for i in range(1, 4):
  key = input(f'Digite o nome do aluno [{i}]: ')
  value = int(input(f'Digite a nota do aluno [{i}]: '))
  students[key] = value

for value in students.values():
  addition += value

print(f'\nMédia dos alunos: {round(addition / 3, 2)}')