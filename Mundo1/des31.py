#desafio 31: custo de viagem //desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Qual a distância da sua viagem? '))
print('=+='*15)
if dist <= 200:
    print(f'\33[1;47mA sua viagem de {dist:.0f}Km custará R${dist*0.50:.2f}\33[m')
else:
    print(f'\33[1;41mA sua viagem de {dist:.0f}Km custará R${dist*0.45:.2f}\33[m')
print('=+='*15)
