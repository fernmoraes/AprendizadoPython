class Carro:
    def __init__(self, marca, modelo):
        #Definindo os atributos do carro
        self.marca = marca
        self.modelo = modelo
    
    def detalhes(self):
        # Método que exibe detalhes do carro
        print(f'Carro marca: {self.marca}, modelo: {self.modelo}')

# Criando um objeto da classe Carro
meu_carro = Carro('Toyota', 'Corola')

#Usando o método da classe
meu_carro.detalhes()

