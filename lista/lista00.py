lista = [4, 6, 8, 10, 67, 10, 40]
cont = 0
for indice in range(len(lista)):
    if lista[indice] % 2 == 0:
        lista[indice] = 0
print(lista)
