# Armazena conjunto de dados organizados sequencialmente, ela não pode ser alterada
tupla = (4, 7, 8)
print(tupla)
print()

# Pode conter diferentes tipos de dados
tupla = (2, 'abc', 4.5, 4)
print(tupla)
print()

# Pode não conter elemento
tupla = ()
print(tupla)
print()

# Tupla com 1 elemento precisa ter vírgula no final
tupla = (10,)       # É uma tupla
print(tupla)

tupla = (10)        # Não é uma tupla
print(tupla)
print()

# Índice
tupla = (4, 6, 7, 8)
print(tupla[0])     # Índice inicial sempre é 0
print(tupla[-1])    # Índices negativos referem ao final da tupla
print()

# Percorrendo Tuplas
for item in tupla:
    print(item)
print()

# Concatenação de Tuplas
tupla1 = (4, 7, 8, 3)
tupla2 = (3, 4)
tupla3 = tupla1 + tupla2
print(tupla3)
print()

# Fatiamento de Tuplas
#tupla[inicio:fim:passo]
tupla = (3, 10, 7, 88, 1, 95, 2, 5, 6)

print(tupla[2:8])
print(tupla[2:8:2])
print(tupla[:])     # Do início ao fim
print(tupla[::2])   # Do início ao fim de 2 em 2
print(tupla[::-1])  # Do fim ao início
print()

# Converter Tupla pra Lista
tupla = (4, 6, 7, 8)
lista = list(tupla)
print(lista)
print()

# Converte uma Lista pra Tupla
lista [4, 6, 7, 8]
tupla = tuple(lista)
print(tupla)