Algoritmo "Maior e Menor"
// Disciplina  : Lógica de Programação e Algoritmos
// Professor   : Adriano Milanez
// Descrição   : Pede-se que o usuário digite dois números, após isto o
// programa irá informar qual número é o maior.
// Autor(a)    : Igor Augusto
// Data atual  : 31/08/2022
Var
// Seção de Declarações das variáveis 
   numero1, numero2: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

    escreva("Informe o valor do primeiro número: ")
    leia(numero1)
    escreva("Informe o valor do segundo número: ")
    leia(numero2)
    
    se (numero1 > numero2) entao
       escreva("O primeiro número é o maior")
    fimse
    
    se numero2 >  numero1 entao
       escreva("O segundo número é o maior")
       
    senao
         escreva("Os dois números são iguais!")
    fimse

Fimalgoritmo