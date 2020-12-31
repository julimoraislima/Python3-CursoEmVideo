#desafio 35: Analisando triângulo V1.0 Para construir um triângulo é necessário que
# a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois
# e maior que o valor absoluto da diferença entre essas medidas.
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

print('\33[1m--=--=-- Analisador de triângulos --=--=--\33[m')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print()
if c < a + b and b < a + c and a < b + c:
    print(f'Os segmentos {a}, {b} e {c} \33[1;32mPODEM\33[m formar um triângulo.')
else:
    print(f'Os segmentos {a}, {b} e {c} \33[1;31mNÃO\33[m podem formar um triângulo.')
print('__'*30)

