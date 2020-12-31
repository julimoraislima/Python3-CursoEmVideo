#desafio 33: Maior e Menor. Programa lê 3 valores, e retorna o maior e o menor valor.
#2-maneira mais composta usando o if

n1 = int(input('Digite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))
n3 = int(input('Digite o terceiro valor inteiro: '))
print('-+-'*20)
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O \33[31mmenor\33[m valor digitado foi \33[31m{menor}\33[m')
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O \33[32mmaior\33[m valor digitado foi \33[32m{maior}\33[m')
print('-+-'*20)


