matriz = []

for i in range(3):
    linha = []
    for j in range(4):
        n = int(input('Numero: '))
        linha.append(n)
    matriz.append(linha)

#Exibe a lista normal
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()

#Trocar os números
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] > 100:
            matriz[i][j] = 0

#Exibe a lista alterada
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()