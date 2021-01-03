#desafio 40: média escolar

from time import sleep
nome = str(input('Digite o nome do aluno: ')).title().strip()
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Analisando...')
sleep(1)
print(' ')
if media < 5:
    print(f'\33[31m{nome} com a média de {media}, foi reprovado!')
elif media == 5 or media < 7:
    print(f'\33[33m{nome} com a média de {media}, está de recuperação!')
else:
    print(f'\33[32mParabéns {nome}! com a média de {media}, foi aprovado!')
print(' ')
print('\33[31m*'*15, '\33[33m*'*15, '\33[32m*'*15)




