#desafio 26: primeira e última ocorrência de uma string

frase = str(input('Digite uma frase: ')).upper().strip()
print('--'*40)
print(f'\33[33mA letra "A" aparece {frase.count("A")} vez/vezes na frase.')
print(f'\33[32mA letra "A" aparece pela primeira vez na posição {frase.find("A")+1}.')
print(f'\33[31mA letra "A" aparece pela última vez na posição {frase.rfind("A")+1}.\33[m')
print('--'*40)



