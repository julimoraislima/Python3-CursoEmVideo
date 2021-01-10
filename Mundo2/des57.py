#desafio 57: Validação de dados. Aceita somente f ou m.

sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos! Digite o sexo [F/M]: ')).upper().strip()[0]
print(f'O sexo {sexo} foi registrado com sucesso!')

