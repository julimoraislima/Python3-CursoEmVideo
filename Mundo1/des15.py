#desafio 15: aluguel de carros ($60 por dia e $0.15 por km rodado

km = float(input('Quantos Km o carro percorreu: '))
dias = float(input('Por quantos dias o carro foi alugado: '))
print('<'*30)
print(f'\33[31mO valor a pagar é de R${km*0.15+dias*60:.2f}\33[m ')
print('>'*30)

