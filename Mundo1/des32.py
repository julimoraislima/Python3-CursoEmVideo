#desafio 32: ano bissexto //
#ano bissexto = 366 dias no ano
#não bissexto = 365 dias no ano
#bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, p.ex: 1996, 2000, 2004, 2008, 2012, 2016, 2020...
#Não são bissextos todos os demais anos.

from datetime import date
ano = int(input('Digite o ano para saber se ele é BISSEXTO ou digite 0 para saber do ano atual: '))
print('='*80)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\33[34mO ano de {ano} é BISSEXTO!\33[m')
else:
    print(f'\33[33mO ano {ano} NÃO é bissexto!\33[m')
print('='*80)
