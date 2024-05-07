# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
# seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
from time import sleep
peso = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))
imc = peso / (altura ** 2)
print('-=' * 25)
print('Aguarde, estamos processando a sua solicitação.')
print('-=' * 25)
sleep(2)
if imc < 18.5:
    print(f'Com um IMC de {imc:.1f} você está abaixo do peso.')

elif imc > 18.5 and imc <= 25:
    print(f'Com um IMC de {imc:.1f} o seu peso é \033[32mideal\033[m.')

elif imc > 25 and imc <= 30:
    print(f'Com um IMC de {imc:.1f} você está com \033[34mSobrepeso\033[m.')

elif imc > 30 and imc <= 40:
    print(f'Com um IMC de {imc:.1f} você está com \033[31mObesidade\033[m.')

elif imc > 40:
    print(f'Com um IMC de {imc:.1f} você está com \033[31mObesidade Mórbida\033[m.')
