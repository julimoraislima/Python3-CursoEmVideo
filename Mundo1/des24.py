#desafio 24: verificando as primeiras letras de um nome (retorna true or false) //se começa com SANTO

city = str(input('Digite o nome da cidade: ')).strip()
print(city[0:5].upper() == 'SANTO')

