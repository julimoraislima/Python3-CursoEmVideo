#desafio 53: Detector de Palíndromo (uma frase que dá para ler ao contrário)
#ex: A sacada da casa  // Usando o FOR in range

frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
print(f'A frase digitada é {junto} e seu inverso é {inverso}.')
if inverso == junto:
    print('->> Portanto é um Palíndromo!')
else:
    print('->> Portanto NÃO é um Palíndromo!')
