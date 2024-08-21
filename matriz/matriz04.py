import random
matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        n = random.randint(1, 50)
        linha.append(n)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()    
        
menor = matriz[0][0]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
print(f'menor: {menor}')