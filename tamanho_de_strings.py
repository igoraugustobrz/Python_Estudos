# Exercício - Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também
# se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

string1 = input("Digite uma frase: ")
string2 = input("Digite outra frase: ")

print("O tamanho de",string1, "é de: ", len(string1), "caracteres")
print("O tamanho de",string2, "é de: ", len(string2), "caracteres")

if len(string1) == len(string2):
    print("As duas string tem o mesmo tamanho.")

else:
    print("As duas strings tem tamanhos diferentes")

if string1 == string2:
    print("As duas strings possuem o mesmo conteúdo")

else:
    print("As duas strings tem conteúdos diferentes")
