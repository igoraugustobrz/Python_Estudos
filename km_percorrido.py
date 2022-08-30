# Entrada de Dados
kmPercorridos = float(input("Digite a quantidade de Km percorridos: "))
diasAlugados = int(input("Informe a quantidade de dias em que o carro foi alugado: "))

# Processamento
kmRodado = kmPercorridos*0.15
diaAlugado = diasAlugados*60
calculaPreco = kmRodado + diaAlugado

# Saída
print("O preço a pagar é R$", calculaPreco)