class Computador:
    def __init__(self, modelo, marca, placa_de_video, memoria_ram):
        self.modelo = modelo
        self.marca = marca
        self.placaDeVideo = placa_de_video
        self.memoriaRam = memoria_ram

    def Ligar(self):
        print(f'Ligando {self.modelo}')

    def Informacoes(self):
        print(f'Marca: {self.marca} | Placa de video: {self.placaDeVideo} | Memoria Ram {self.memoriaRam}')

    def Desligar(self):
        print(f'Desligando {self.modelo}')

modelo = input('Insira o modelo: ')
marca = input('Insira a marca: ')
placaDeVideo = input('Insira a placa de vídeo: ')
memoriaRam = input('Insira a memoria ram')

computador1 = Computador(modelo, marca, placaDeVideo, memoriaRam)
computador1.Ligar()
computador1.Informacoes()
computador1.Desligar()