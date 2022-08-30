# Entrada de Dados
cigarrosPorDia = int(input("Informe quantos cigarros você fuma por dia: "))
anosFumados = int(input("Informe há quanto tempo você fuma: "))

# Processamento
reducao_em_minutos = anosFumados * 365 * cigarrosPorDia * 10
reducao_em_dias = reducao_em_minutos/ (24*60)

# Saída
print("Você já perdeu", round(reducao_em_dias) ,"dias")