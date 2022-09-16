valorCasa = float(input("Digite o valor da casa: "))
salarioIndividuo = float(input("Informe o seu salário: "))
pagarAnos = float(input("Você pretende pagar a compra em quantos anos?\n"))

converteAnos = pagarAnos * 12
salario30 = (30 * salarioIndividuo)/100
prestacaoMensal = valorCasa/converteAnos

if prestacaoMensal >= salario30:
    print("Empréstimo negado")

else:
    print("Empréstimo aprovado")
