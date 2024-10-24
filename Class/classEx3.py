class Cachorro:
    def __init__(self, nome, idade):
        # Quando criamos um novo cachorro, ele vai ter um nome e uma idade
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        # Esse método faz o cachorro latir
        print("Au au!")

# Lista para armazenar os cachorros criados
lista_de_cachorros = []

quantidade = int(input('Quantos cachorros você quer criar?: '))

for i in range(quantidade):
    nome= input(f'Digite o nome do cachorro {i + 1}: ')
    idade = int(input(f'Digite a idade do cachorro {i + 1}: '))
    # Criando o cachorro e adicionando ele na lista
    novo_cachorro = Cachorro(nome, idade)
    lista_de_cachorros.append(novo_cachorro)

# Mostrando todos os cachorros cadastrados
print('\nAqui estão os cachorros que você cadastrou:')
for cachorro in lista_de_cachorros:
    print(f'Cachorro: {cachorro.nome}, {cachorro.idade} anos')
    cachorro.latir()
