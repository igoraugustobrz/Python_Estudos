genero = input("Informe o seu genero: ").upper()
altura = float(input("Digite a sua altura: "))

if genero == "HOMEM":
    formulaHomens = (72.7 * altura) - 58
    print("O seu peso ideal é: ", formulaHomens)

elif genero == "MULHER":
    formulaMulheres = (62.1 * altura) - 44.7
    print("O seu peso ideal é: ", formulaMulheres)