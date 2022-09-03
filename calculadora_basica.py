# Entrada de Dados
numero1 = int(input("Informe o valor do primeiro número: "))
numero2 = int(input("Informe o valor do segundo número: "))

# Processamento
operacao = int(input("Informe a operação desejada, sendo: 1 - Soma, 2 - Subtração, 3 - Multiplicação e 4 - Divisão\n"))

soma = numero1 + numero2 
sub = numero1 - numero2
mult = numero1 * numero2
div = numero1/numero2

if operacao == 1:
   print("O resultado da adição é: ", soma)
   
elif operacao == 2:
    print("O resultado da subtração é: ", sub)
    
elif operacao == 3:
    print("O resultado da multiplicação é: ", mult)

elif operacao == 4:
    print("O resultado da divisão é: ", div)

else:
    print("ERROR! Operação não válida.")
