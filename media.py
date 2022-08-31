# Entrada de Dados
materia1 = float(input("Digite a nota da primeira matéria: "))
materia2 = float(input("Digite a nota da segunda matéria: "))

# Processamento
media = (materia1 + materia2)/2

# Saída de Dados
if media >= 6:
    print("Você foi aprovado, campeão!")
else:
    print("Hm... Precisa estudar")