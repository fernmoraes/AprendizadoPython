'''
Classe é um modelo que define a estruturae o comportamento de objetos.
Objetos são instâncias de classes.
'''

'''
Criando uma classe
Sintaxe básica para criar a classe
'''

class NomeDaclasse:
    
    #Metodo Construtor, é chamado quando um novo objeto é criado
    def __init__(self, valor):  #self é sempre primeiro e refere-se ao próprio objeto
        #define os atributos do objeto
        self.atributo1 = valor
        self.atributo2 = valor
    
    #Método da classe
    def metodo(self):
        #Comportamento do objeto
        print('isso é um metodo')