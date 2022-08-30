precoDaMarmita = float(input("Digite o preço da mercadoria: "))
percentualDeDesconto = int(input("Digite o percentual de desconto: "))

formulaDesconto = percentualDeDesconto/100

print("O percentual de desconto do produto é: ", abs((formulaDesconto*precoDaMarmita) - precoDaMarmita))
1