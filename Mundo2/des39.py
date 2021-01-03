#desafio 39: alistamento militar

from datetime import date
atual = date.today().year
sexo = int(input('''Informe o seu sexo:
[1] para sexo masculino
[2] para sexo feminino
Opção: '''))
masculino = 1
feminino = 2
if sexo == 2:
    print('-+'*40)
    print('Você não precisa se alistar!')
else:
    nasc = int(input('Digite o ano do seu nascimento: '))
    idade = atual - nasc
    falta = 18 - idade
    passou = idade - 18
    quandosera = atual + falta
    quandofoi = atual - passou
    print('-+'*40)
    print(f'A sua idade é {idade} anos.')
    if idade == 18:
        print('Você deve se alistar IMEDIATAMENTE.')
    elif idade < 18:
        print(f'Ainda falta {falta} anos para seu alistamento, que será em {quandosera}.')
    elif idade > 18:
        print(f'Já se passou {passou} anos do prazo de alistamento, que foi em {quandofoi}.')
print('-+'*40)

