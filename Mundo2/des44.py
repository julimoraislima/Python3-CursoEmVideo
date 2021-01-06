#desafio 44: Gerenciador de pagamento

print('===+==+==+== LOJA BARATESS ==+==+==+===')
produto = float(input('Digite o valor atual do produto: R$ '))
print('''Em que condições quer pagar: 
[1] À vista com dinheiro/cheque (10% de desconto)
[2] À vista com cartão (5% de desconto)
[3] Em até 2x no cartão (preço normal)
[4] 3x ou mais no cartão (20% de juros)''')
opcao = int(input('Sua opção: '))
opcao1 = produto - (produto * 10/100)
opcao2 = produto - (produto * 5/100)
opcao3 = produto / 2
opcao4 = produto + (produto * 20/100)
if opcao == 1:
    print(f'O produto passará a valer: R${opcao1:.2f}')
elif opcao == 2:
    print(f'O produto passará a valer R${opcao2:.2f}')
elif opcao == 4:
    vezes = int(input('Em quantas vezes: '))
    parcela = opcao4 / vezes
    print(f'O produto de R${opcao4:.2f} em {vezes}x de R${parcela:.2f} cada parcela.')
elif opcao == 3:
    print(f'O produto no valor de R${produto:.2f} em 2x sem juros de R${opcao3:.2f} cada parcela.')
else:
    print('Opção inválida, tente novamente.')
