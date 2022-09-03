# Entrada de Dados
valor1= float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))
valor3 = float(input("Informe o terceiro valor: "))

# Processamento e Saída 
if valor1 > valor2 and valor1 > valor3:
    print("O primeiro valor é o maior")
    
if valor2 > valor1 and valor2 > valor3:
    print("O segundo valor é o maior")

if valor3> valor1 and valor3 > valor2:
    print("O terceiro valor é o maior")
    
# Detecta qual dos três valores é o menor
if valor1 < valor2 and valor1 < valor3:
    print("O primeiro valor é o menor")
   
if valor2 < valor1 and valor2 < valor3:
    print("O segundo valor é o menor")
    
if valor3 < valor1 and valor3 < valor2:
    print("O terceiro valor é o menor")