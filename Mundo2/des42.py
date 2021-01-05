#desafio 42: Analizando triângulo V.2.0 - EQUILÁTERO: todos os lados iguais.
# -ISÓSCELES: dois lados iguais, um diferente. - ESCALENO: todos os lados diferentes.

print('\33[1m--=--=-- Analisador de triângulos --=--=--\33[m')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print('->'*4, end=' ')
if c < a + b and b < a + c and a < b + c:
    print('Os segmentos acima PODEM formar um triângulo ', end='', )
    if a == b == c:
        print('\33[34mEQUILÁTERO.')
    elif a != b != c != a:
        print('\33[33mESCALENO.')
    else:
        print('\33[32mISÓSCELES.')
else:
    print('\33[31mOs segmentos acima NÃO podem formar um triângulo.')

