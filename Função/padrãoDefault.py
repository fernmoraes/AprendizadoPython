#Parametro default (padrão)

def cadastrar_funcionario(nome:str='Não Informado', idade:int=0, salario:float=0.0):
    print('-'*30)
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f'Salario: {salario}')

#PArâmentro Posicional
cadastrar_funcionario('Francisco', 30, 2500.0) #3 infos
cadastrar_funcionario('Francisco', 30) #2 infos
cadastrar_funcionario('Francisco') #1 info

#Parâmetro Nomeado
cadastrar_funcionario(idade= 27,) #informei só a idade
cadastrar_funcionario(salario=3000, nome='Robertinho', idade=30) #Com o nome, pode fazer fora de ordem

#Parâmetro Posicional e Nomeado na mesma fun
#Primeiro o Posicional e depois o Nomeado
cadastrar_funcionario('Franciso', salario=2500.0)
