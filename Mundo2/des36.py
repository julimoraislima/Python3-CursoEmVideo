#desafio 36: aprovando empréstimos /se a prestação for maior que 30% do salário-empréstimo negado.

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário mensal do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = (casa / anos) / 12   #casa/(anos*12)
minimo = salario * 30/100
print(f'A casa no valor de R${casa:.2f} paga em {anos} anos, terá uma prestação mensal de R${prestacao:.2f}')
print('--'*45)
if prestacao <= minimo:
    print('\33[32mO empréstimo pode ser CONCEDIDO!\33[m')
else:
    print('\33[31mO empréstimo foi NEGADO!\33[m')
