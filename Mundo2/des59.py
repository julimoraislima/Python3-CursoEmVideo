#desafio 59: Criando um menu de opções. Leia 2 valores e mostre um menu.

from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Escolher novos números
    [5] Sair do programa''')
    opcao = int(input('>>>> Sua Opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'\33[36mA soma dos números {n1} + {n2} é: {soma}.\33[m')
        print('-+-' * 20)
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'\33[36mA multiplicação dos números {n1} x {n2} é: {multiplicar}.\33[m')
        print('-+-'*20)
    elif opcao == 3:
        lista = [n1, n2]
        print(f'\33[36mO número maior digitado foi {max(lista)}.\33[m')
        print('-+-' * 20)
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print('-+-' * 20)
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
        print('-+-' * 20)
        print('Fim do programa. Volte sempre!')
    else:
        print('\33[31mOpção inválida! Tente novamente.\33[m')
        print('-+-' * 20)



