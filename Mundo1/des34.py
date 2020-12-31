#desafio 34: Aumentos múltiplos. Se salário inicial for <=1250 terá 15% de aumento,
# ao contrário terá um aumento de 10%.

salarioinicial = float(input('Digite o valor do salário atual: R$'))
print()
print('>'*10, end=' ')
if salarioinicial <= 1250.00:
    salariofinal = salarioinicial + (salarioinicial * 15/100)
    print(f'O salário de \33[1;33mR${salarioinicial:.2f}\33[m com o aumento de \33[34m15%\33[m passará a ser de \33[31mR${salariofinal:.2f}\33[m')
else:
    salariofinal = salarioinicial + (salarioinicial * 10/100)
    print(f'O salário de \33[1;33mR${salarioinicial:.2f}\33[m com o aumento de \33[34m10%\33[m passará a ser de \33[31mR${salariofinal:.2f}\33[m')


