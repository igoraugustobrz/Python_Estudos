# ======= Exercício =======
# 1. Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
# - Números
# - CEPs
# - URLs

import regex

print(f'======= Regular Expression =======\n')

text = 'Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e meu site é https://www.iaexpert.academy'

numbers = regex.findall(r'\d', text)
cep = regex.findall(r'\d{5}-\d{3}', text)
url = regex.findall(r'https?://[A-Za-z0-9./]+', text)

print(f'Resultado - Expressões regulares:\nNúmeros: {numbers}\nCEP: {cep}\nUrl: {url}')