#desafio 56: Analisador completo. Nome, idade e sexo de 4 pessoas e mostra a média de idade
#do grupo, o homen mais velho e quantas mulheres abaixo de 20 anos.

import statistics
idadehomemvelho = 0
nomehomemvelho = ''
listidade = []
contmulher = 0
for pessoa in range(1, 5):
    print(f'---------- {pessoa}ª PESSOA ----------')
    nome = str(input('NOME: ')).strip().title()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [F/M]: ')).strip()
    listidade += [idade]
    if pessoa == 1 and sexo in 'Mm':
        idadehomemvelho = idade
        nomehomemvelho = nome
    if sexo in 'Mm' and idade > idadehomemvelho:
        idadehomemvelho = idade
        nomehomemvelho = nome
    if idade < 20 and sexo in 'Ff':
        contmulher += 1
print('\33[1;34m------------------ RESULTADO ---------------------\33[m')
print(f'\33[34mA média de idade do grupo é de {statistics.mean(listidade)} anos.')
print(f'O homem mais velho tem {idadehomemvelho} anos e seu nome é {nomehomemvelho}.')
print(f'Ao todo são {contmulher} mulher/es com menos de 20 anos.')
print('\33[1;34m-\33[m'*50)

