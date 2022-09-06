primeiroFator = int(input("Digite o primeiro número: "))
segundoFator = int(input("Digite o segundo número: "))
contador = 1
produto = 0

while contador <= segundoFator:
    produto = produto + primeiroFator
    contador = contador + 1

print(primeiroFator, "x", segundoFator, " = ", produto)
    