quantidade = int(input('Quantos números você deseja calcular? '))
lim = 1
cont = 0
listaPar = []
listaImpar = []

while lim <=quantidade:
    num = int(input(f'[{cont}/{quantidade}] Insira um número: '))
    lim += 1
    cont += 1
    if num % 2 != 0:
        listaImpar.append(num)
    else:
        listaPar.append(num)

somaPar = sum(listaPar) #sum soma a lista
quantidadePar = len(listaPar) #len conta a quantidade de elementos dentro da lista
mediaPar = somaPar / quantidadePar

somaImpar = sum(listaImpar)
quantidadeImpar = len(listaImpar)
mediaImpar = somaImpar / quantidadeImpar

print(f'De um total de {quantidade} números, {quantidadePar} são pares com a média {mediaPar}, {quantidadeImpar} são impares com a média {mediaImpar}')