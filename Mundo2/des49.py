#desafio 49: Tabuada V.2.0

n = int(input('Digite um número inteiro: '))
print('-'*12)
for c in range(1, 11):
    print(f'\33[1;36m{n} x {c:2} = {n*c}\33[m')   #{:2} = 2 dígitos para alinhar a segunda coluna
print('-'*12)


