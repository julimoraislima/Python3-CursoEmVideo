#desafio 61: Progressão Aritmética V.2.0

print('='*40)
print(' '*10, end=' ')
print('10 TERMOS DE UMA PA v2.0')
print('='*40)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'\33[1;34m{termo}', end=' ► ')
    termo += razao
    cont += 1
print('ACABOU')
