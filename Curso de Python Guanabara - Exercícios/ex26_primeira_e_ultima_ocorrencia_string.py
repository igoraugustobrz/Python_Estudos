# Faça um programa que leia uma frase pelo teclado e mostre:
#  - Quantas vezes aparece a letra “A”;
#  - Em que posição ela aparece a primeira vez;
#  - Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A apareceu ', frase.count('A'), ' vezes na frase')
print('A primeira letra A apareceu na posição ', frase.find('A') + 1)
print('A última letra A aparece na posição ', frase.rfind('A') + 1)