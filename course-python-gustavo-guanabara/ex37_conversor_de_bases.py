#  Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
#  conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um número inteiro: '))
opcao = int(input('Sendo: 1 - Binário, 2 - Octal e 3 - Hexadecimal. Escolha: '))
if opcao == 1:
    print(f'O número {n} em bin é {bin(n)[2:]}')
elif opcao == 2:
    print(f'O número {n} em oct é {oct(n)[2:]}')
elif opcao == 3:
    print(f'O número {n} em hex é {hex(n)[2:]}')
else:
    print('Opção inválida. Tente novamente.')