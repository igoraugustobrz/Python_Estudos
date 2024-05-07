# Crie uma tupla preenchida com 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação, depois mostre:
# Os 5 primeiros
# Os 4 últimos
# Times em ordem alfabética
# Em que posição está o time do 'Santos'
tupla = ('América Mineiro', 'Bahia', 'Botafogo', 'Brasil de Pelotas', 'Corinthians', 'Coritiba', 'Cuiabá', 'Cruzeiro', 'CSA', 'Flamengo',
'Guarani', 'Ituano', 'Juventude', 'Londrina', 'Náutico', 'Palmeiras', 'Santos', 'Tombense', 'Vasco', 'Vila Nova')
print(f'Cinco primeiros: {tupla[0:6]}')
print(f'Quatro últimos: {tupla[-4:]}')
print(f'Times em ordem alfabética: {tupla}')
print('O Santos está na posição', tupla.index('Santos'))