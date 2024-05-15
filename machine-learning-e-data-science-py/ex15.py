# ======= Exercício =======
# 1. Crie uma classe chamada aluno com os seguintes atributos:
# - Nome
# - Nota 1
# - Nota 2
# - Crie um construtor para a classe (__init__)

# 2. Crie as seguintes funções (métodos):
# - Calcula média, retornando a média aritmética entre as notas
# - Mostra dados, que somente imprime o valor de todos os atributos
# - Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)

# 3. Crie dois objetos (aluno1 e aluno2) e teste as funções

class Aluno:
    def __init__(self, nome, n1, n2):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.media = 0.0
    
    def calculaMedia(self):
        self.media = (self.n1 + self.n2) / 2 
        return self.media
  
    def mostraDados(self):
        print(f'======= Dados: =======\n\nNome: {self.nome}\n1º Nota: {self.n1}\n2º Nota: {self.n2}\nMédia: {self.media}')
    
    def resultado(self):
        if self.media >= 6:
            print('Aluno aprovado')
        else:
            print('Aluno reprovado')
      
aluno1 = Aluno('Igor', 9.0, 9.0)
aluno1.calculaMedia()
aluno1.resultado()
aluno1.mostraDados()
