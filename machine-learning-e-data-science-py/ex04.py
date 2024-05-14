'''
======= Exercício =======

1. Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas N1, N2 e N3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
- Se a média for maior do que 6.0, o aluno está aprovado
- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado
'''

print('======= Programação I - Média =======\n')

n1 = float(input('Informe a 1º nota: '))
n2 = float(input('Informe a 2º nota: '))
n3 = float(input('Informe a 3º nota: '))

avg = round((n1 + n2 + n3) / 3, 2)

if avg > 6:
  print('\nAluno aprovado')
  
elif avg >= 4.1 and avg <= 6.0:
  print('\nAluno pegou exame')
  exam = float(input('\nInforme a nota do exame: '))
  if exam > 6:
    print('\nAluno aprovado no exame')
  else:
    print('\nAluno reprovado no exame')
    
else:
  print('\nAluno reprovado')
