kwhConsumido = float(input("Digite a quantidade de Kwh consumido: "))
tipoInstalacao = input("Informe o tipo de instalação, sendo R - Residencial, C - Comércio e I - Industrial ").upper()

if tipoInstalacao == "R" and kwhConsumido <= 500:
    print("O preço a pagar pelo fornecimento de energia do tipo R1 é de R$", round(kwhConsumido * 0.40))

elif tipoInstalacao == "R" and kwhConsumido > 500:
    print("O preço a pagar pelo fornecimendo de energia do tipo R2 é de R$", round(kwhConsumido * 0.65))

elif tipoInstalacao == "C" and kwhConsumido <= 1000:
    print("O preço a pagar pelo fornecimento de energia do tipo C1 é de R$", round(kwhConsumido * 0.55))

elif tipoInstalacao == "C" and kwhConsumido > 1000:
    print("O preço a pagar pelo fornecimento de energia do tipo C2 é de R$", round(kwhConsumido * 0.60))

elif tipoInstalacao == "I" and kwhConsumido <= 5000:
    print("O preço a pagar pelo fornecimento de energia do tipo I1 é de R$", round(kwhConsumido * 0.55))

elif tipoInstalacao == "I" and kwhConsumido > 5000:
    print("O preço a pagar pelo fornecimento de energia do tipo I2 é de R$", round(kwhConsumido * 0.60))

else:
    print("Tipo de instalação incorreta.")

