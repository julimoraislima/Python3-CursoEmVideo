#desafio 41: classificando atletas de acordo com a idade

from datetime import date
nasc = int(input('Digite o ano do nascimento do atleta: '))
atual = date.today().year
idade = atual - nasc
print('>>>', '-'*50, '>>>')
if idade <= 9:
    print(f'\33[31mA idade do atleta é {idade} anos e sua categoria é MIRIM.\33[m')
elif 14 >= idade > 9:
    print(f'\33[35mA idade do atleta é de {idade} anos e sua categoria é INFANTIL.\33[m')
elif 19 >= idade > 14:
    print(f'\33[34mA idade do atleta é de {idade} anos e sua categoria é JUNIOR.\33[m')
elif 25 >= idade > 19:
    print(f'\33[32mA idade do atleta é de {idade} anos e sua categoria é SENIOR.\33[m')
elif idade > 25:
    print(f'\33[33mA idade do atleta é de {idade} anos e sua categoria é MASTER.\33[m')
print('<<<', '-'*50, '<<<')



