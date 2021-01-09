#desafio 54: Grupo de maioridade

from datetime import date
atual = date.today().year
menores = 0
maiores = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Digite o ano que a {pessoa}ª pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 21:
        maiores = maiores + 1
    else:
        menores += 1
print('-'*40)
print(f'*** Entre as 7 pessoas, \33[32m{maiores} são MAIORES \33[me \33[31m{menores} são MENORES.\33[m ***')


