'''
Definição:
Trata-se de um processo, onde procura-se selecionar, utilizando um critério específico, alguma informação
particular, a partir de uma coleção de dados
'''
'''
A Escolha do método mais adequado depende:
Da quantidade de dados envolvidos
Da ordenação inicial dos dados
Da lista estar sujeita a inserções e retiradas contantes
'''

'''
Python já oferece funções de buscasmas não tão eficientes
'''

'''
Busca Linear:
Mais simples
Pode ser usado em listas não ordenadas
Menos eficiente
Se a lista toda for percorrida retorna -1
'''
'''
Busca Binária:
É um pouco mais sofisticado
'''

def buscar_linear(lista, item):
    #Percorre lista do índice 0 a n-1
    for i in range(len(lista)):
        if lista[i] == item:
            return 'True' #ou i        #Encontrou elemento na posição i
    return 'False'  #ou -1               #Não encontrou item                       

def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:     #Encontrou item
            return 'True' #ou meio            #Retorna índice
        elif item > lista[meio]:    #Busca na segunda metade
            inicio = meio + 1
        else:                       #Busca na primeira metade
            fim = meio -1
    return 'False' #ou -1                       #Não encontrou o item


tamanho = int(input('Digite o tamanho da lista: '))
lista = []

for n in range(0, tamanho):
    lista.append(n+1)

item = int(input('Digite o número que deseja procurar: '))
busca = int(input('[1] Para busca linear | [2] Para busca binaria: '))
if busca == 1:
    print(buscar_linear(lista, item))
elif busca == 2:
    print(busca_binaria(lista, item))
else:
    print('Opção inválida')