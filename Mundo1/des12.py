#desafio 12: calculando desconto

valor = float(input('Digite o preço do produto: R$'))
desc = float(input('Digite o desconto em %: '))
valorfinal = valor - (valor * (desc/100))
print('\33[31m>\33[m'*70)
print(f'O produto de valor R${valor:.2f} com desconto de {desc}% valerá R${valorfinal:.2f}')
print('\33[31m>\33[m'*70)

