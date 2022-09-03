numero = int(input("Tabuada de: "))
fimTabuada = int(input("Fim da tabuada: "))

contador = 0
tabuada = 0
    
while contador <= fimTabuada:
   tabuada = numero * contador  
   print("\n", numero, " x ", contador, " = ", tabuada)
   contador = contador + 1