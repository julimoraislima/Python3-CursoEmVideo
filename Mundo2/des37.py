#desafio 37: conversor de bases numéricas

print('>>>>> CONVERSOR DE BASES NUMÉRICAS <<<<<')
num = int(input('\33[31mDigite um número inteiro: \33[m'))
print('''[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opcao = int(input('\33[31mSua opção: \33[m'))
print('>>>> ', end='')
if opcao == 1:
    print(f'O número {num} convertido em Binário é: {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convertido em Octal é: {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} convertido em Hexadecimal é: {hex(num)[2:]}')
else:
    print('Opção inválida!')

