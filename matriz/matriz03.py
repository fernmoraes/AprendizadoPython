from random import randint

matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        n_Aleatorio = randint(1, 100)
        linha.append(n_Aleatorio)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()

#Soma da diagonal
diagonal = []
for l in range(len(matriz)):
    num = matriz[l][l] #ou fazer num += matriz[l][l]
    diagonal.append(num)

soma = sum(diagonal)
print(f'A soma da diagonal é {soma}')
