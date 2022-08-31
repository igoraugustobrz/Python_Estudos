contaDoCliente = int(input("Informe os números da conta: "))
saldo = float(input("Informe o seu saldo: "))
debito = float(input("Informe o débito:"))
credito = float(input("Informe o crédito: "))

saldoAtual = saldo - debito + credito 

if saldoAtual >= 0:
    print("Saldo positivo!")
    
else:
    print("Saldo negativo!")