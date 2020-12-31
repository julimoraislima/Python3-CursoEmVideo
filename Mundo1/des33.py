#desafio 33: Maior e Menor. Programa lê 3 valores, e retorna o maior e o menor valor.
#1-maneira simplificada usando uma lista[].

primeiro = int(input('Digite o primeiro valor inteiro: '))
segundo = int(input('Digite o segundo valor inteiro: '))
terceiro = int(input('Digite o terceiro valor inteiro: '))
numeros = [primeiro, segundo, terceiro]
print('-+-'*20)
print(f'O \33[31mmaior\33[m valor digitado foi \33[31m{max(numeros)}\33[m')
print(f'O \33[32mmenor\33[m valor digitado foi \33[32m{min(numeros)}\33[m')
print('-+-'*20)


