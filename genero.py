# Exercício - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra
# escrever: F - Feminino, M - Masculino, Sexo Inválido.

genero = input("Informe o seu gênero, sendo F para feminino e M para masculino: \n").upper()

if genero == "M":
    print("Sexo masculino")
        
elif genero == "F":
    print("Sexo feminino")
        
else:
    print("Sexo inválido!")