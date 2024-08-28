# Dicionário vazio
dicionario0 = {}

# Dicionário
dicionario1 = {'name': 'Bob',
               'age': 25,
               'job': 'Dev'}

print(dicionario1)
print()

# Acessar um valor do dicionário
print(dicionario1['name'])
print()

# Alterar um item
dicionario1['age'] = 26
print(dicionario1)
print()

# Inserir um item
dicionario1['city'] = 'São Paulo'
print(dicionario1)
print()

# Remover item
dicionario1.pop('city')
print(dicionario1)
print()

# Percorrer as chaves do dicionário
for chaves in dicionario1.keys():
    print(chaves)
print()

for chaves in dicionario1.keys():
    if chaves == 'name':
        print('Tem')
print()

if 'age' in dicionario1:
    print('A chave "age" existe')
else:
    print('A chave "age" não existe')
print()

# Percorrer os valores do dicionário
for valor in dicionario1.values():
    print(valor)
print()

# Percorrer os chaves e valores do dicionário
for chave, valor in dicionario1.items():
    print(chave, valor)
print()

# Dicionário no dicionário
alunos = {'rm1234': {'nome': 'Ana', 'notas': [7, 8, 10]},
          'rm5678': {'nome': 'João', 'notas': [9.6, 10, 5]}}
print(alunos['rm1234']['nome'])
print(alunos['rm5678']['notas'][2])
