#desafio 73: Tuplas com times de futebol

brasileirao = 'Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',\
    'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',\
    'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Ceará', 'Sport Recife',\
    'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Petra', 'Atlético-GO'
print(f'\33[37mOs times do Brasileirão são: {brasileirao}')
print(f'\33[35mA) Os 5 primeiros times são: {brasileirao[0:5]}')
print(f'\33[34mB) Os 4 últimos times são: {brasileirao[17:]}')
print(f'\33[32mC) Os times em ordem alfabética: {sorted(brasileirao)}')
print(f'\33[31mD) O time {brasileirao[7]} está na 8ª posição.')
