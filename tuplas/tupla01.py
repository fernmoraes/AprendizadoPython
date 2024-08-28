def maior_menor_media(lista: list) -> tuple:
    """Retorna uma tupla com o maior, menor e média de uma lista"""
    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)
    return maior, menor, media          # retorna uma tupla com 3 itens


lista = []
for i in range(10):
    n = int(input('Numero: '))
    lista.append(n)
print(lista)

resultado = maior_menor_media(lista)

print(f'Maior: {resultado[0]}')         # acessa as posições da tupla de retorno da função
print(f'Menor: {resultado[1]}')
print(f'Média: {resultado[2]}')
