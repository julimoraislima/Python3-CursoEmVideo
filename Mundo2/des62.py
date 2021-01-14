#desafio 62: Super Progressão Aritmética V.3.0 (digite 0 para sair)

from time import sleep
print('='*40)
print(' '*10, end=' ')
print('10 TERMOS DE UMA PA v3.0')
print('='*40)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
maistermos = 10
while maistermos != 0:
    total = total + maistermos
    while cont <= total:
        print(f'\33[1;36m{termo}', end=' ► ')
        termo += razao
        cont += 1
    print('Pausa!\33[m')
    maistermos = int(input('Quantos termos quer mostrar a mais?: '))
print('\33[1;37mFinalizando..\33[m')
sleep(1)
print(f'\33[1;37m>>>>>>> Progressão finalizada com {total} termos!\33[m')
