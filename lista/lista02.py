lista = [1, 4, 6, 6, 10, 8]

# sort (ordena uma lista)
lista.sort()
lista.sort(reverse=True)

#sorted (retorna uma cópia ordenada de uma lista)
lista2 = sorted(lista)

# max (retorna o maior valor)
maior = max(lista)

# min (retorna o menor valor)
menor = min(lista)

# sum (retorna o somatório)
soma = sum(lista)

# media da lista
media = sum(lista) / len(lista)

#concatenação (junção lista)
lista3 = lista + lista2 + lista

# copy (copia a lista)
lista4 = lista.copy()