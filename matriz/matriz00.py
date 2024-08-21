#preencher matriz 3x4
matriz = []

for i in range(3):  #repete 3 vezes
    linha = []  #Cria lista
    for j in range(4): #Repete 4 vezes
        n = int(input('Numero: ')) #Você insere um número 4 vezes, salva em uma lista
        linha.append(n) #Insere essa lista na matriz principal
    matriz.append(linha)

#exibe a matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()

#somatorio da matriz
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        soma += matriz[i][j]
print(f'Somatório: {soma}')

#somatorio pares da matriz
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
print(f'Somatório dos pares: {soma}')