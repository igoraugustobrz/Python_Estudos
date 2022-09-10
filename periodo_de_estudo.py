# Exercício - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou
# N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

periodoDeEstudo = input("Digite o seu período de estudo, sendo M para matutino, V para Vespertino e N para noturno: ").upper()

if periodoDeEstudo == "M":
    print("Bom dia!")

elif periodoDeEstudo == "V":
    print("Boa tarde!")

elif periodoDeEstudo == "N":
    print("Boa noite!")

elif periodoDeEstudo != "M" and "V" and "N":
    print("Período inválido!")