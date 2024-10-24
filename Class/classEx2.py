class Cachorro:
    def __init__(self, nome, idade):
        # Quando criamos um novo cachorro, ele vai ter um nome e uma idade
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        # Esse método faz o cachorro latir
        print("Au au!")

cachorro1 = Cachorro("Rex", 5)
cachorro2 = Cachorro("Buddy", 3)

cachorro1.latir()
cachorro2.latir()

print(f"Cachorro 1: {cachorro1.nome}, {cachorro1.idade} anos.")
print(f"Cachorro 2: {cachorro2.nome}, {cachorro2.idade} anos.")
