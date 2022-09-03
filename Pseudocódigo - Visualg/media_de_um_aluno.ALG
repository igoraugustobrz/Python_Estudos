Algoritmo "semnome"
// Disciplina   : Lógica de Programação e Algoritmos
// Professor   : Adriano Milanez
// Descrição   : Calcula a média de duas notas de um aluno
// e imprime na tela se foi aprovado, reprovado ou aprovado
// com louvor (nota 10)
// Autor(a)    : Igor Augusto
// Data atual  : 25/08/2022
Var
// Seção de Declarações das variáveis 
   nota1, nota2, media:real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   escreva("Informe a nota1: ")
   leia(nota1)

   escreva("Informe a nota2: ")
   leia(nota2)
   
   media <-(nota1 + nota2)/2
   
   se media >= 7 e media <> 10 entao
      escreva("Parabéns meu bom!")
   fimse

   se media = 10 entao
      escreva("Aprovado com louvor!!! (nota 10)")

   senao
        escreva("Mais um ano com o André")
   fimse
   
Fimalgoritmo