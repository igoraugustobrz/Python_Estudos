distanciaPercorrer = float(input("Digite a distância que você deseja percorrer: "))
precoViagensCurtas = 0.50
precoViagensLongas = 0.45


if distanciaPercorrer <= 200:
    print("O preço da passagem para viagens curtas ficou num total de R$", precoViagensCurtas*distanciaPercorrer)

else:
    print("O preço da passagem para viagens longas ficou num total de R$", precoViagensLongas*distanciaPercorrer)