# Set é um conjunto de itens definidos entre chaves {}
# Diferente do dicionário, ele não possui os dois pontos :, ele é separado por apena vírgula
# Não possui uma ordem especifica

# Conjunto vazio
conjunto = set()

# Conjunto
conjunto = {'Banana', 'Maçã', 'Cereja', 3, 50}
print(conjunto)

# Verificar se um item está contido no conjunto
if 3 in conjunto:
    print('Esta contido')
else:
    print('Não está contido')

# Percorrer conjunto
for item in conjunto:
    print(item)

# Tamanho de um conjunto
print(len(conjunto))

# Um conjunto não permite itens repetidos
conjunto = {3, 50, 50, 3, 50, 3, 70}
print(conjunto)

# Adicionar item no conjunto
conjunto.add(10)
print(conjunto)

# Remover item (remove) - gera um erro se o item não existir
conjunto.remove(10)
print(conjunto)

# Remover item (discard) - Não gera um erro se o item não existir
conjunto.discard(100)
print(conjunto)

# União de conjuntos
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)
print(set3)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {9, 10, 11, 12}
set4 = set1 | set2 | set3
print(set4)

# Interseção de conjuntos
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.intersection(set2)
print(set3)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1 & set2
print(set3)

# Diferença entre conjuntos
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.difference(set2)
print(set3)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1 - set2
print(set3)

# Diferença simétrica entre conjuntos
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1 ^ set2
print(set3)

# Gera um conjunto a partir de uma lista
nomes = ['Ana', 'João', 'Pedro', 'Ana', 'Marcos']
conjunto = set(nomes)
print(conjunto)

# Remover letras repetidas
nomes = 'exemplo de texto para remover palavras do texto'
conjunto = set(nomes)
print(conjunto)

# Remove os itens repetido
nomes = 'exemplo de texto para remover palavras do texto'
lista = nomes.split()
conjunto = set(lista)
print(conjunto)
lista = list(conjunto)
print(lista)

# PReencher um conjunto com inputs
conjunto = set()
for i in range(5):
    n = int(input('Numero: '))
    conjunto.add(n)
print(conjunto)