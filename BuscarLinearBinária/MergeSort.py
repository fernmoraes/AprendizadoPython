'''
Merge Sort
- Técnica de divisão, divide sempre a lista em 2 construindo uma nova lista
Possui 2 funções utilizadas na implementação do Merge Sort
- merge_sort: é a função que divide a lista em sublistas
- intercala: éafunção que intercala duas sublistas em uma lista ordenada
'''
'''
-O desempenho do MergeSort não é impactado pela disposiçãoinicial dos itens da lista
-O algortimo apresenta tanto no pior caso quanto no melhor caso um tempo de execução linear de comparações,
em função do tamanho da lista.
-O tempo de execução é n log n
'''

def intercala(lista, inicio, meio, fim):
    aux = []                                # lista auxiliar
    esq = inicio
    dir = meio + 1
    while(esq <= meio and dir <= fim):      # enquanto não avaliou completamente
        if (lista[esq] <= lista[dir]):      # uma das sublistas, copia o menor
            aux.append(lista[esq])          # elemento para lista auxiliar
            esq += 1
        else:
            aux.append(lista[esq])
            dir += 1
    while(esq <= meio):                     # copia o resto da primeria sub-lista
        aux.append(lista[esq])
        esq += 1
    while(dir <= fim):                      # copia o resto da segunda sub-lista
        aux.append(lista[dir])
        dir += 1
    lista[inicio:fim+1] = aux               # copia a lista auxiliar paraa lista
    return lista


def merge_sort(lista, inicio, fim):
    meio = (fim + inicio) // 2
    if (inicio < fim):
        merge_sort(lista, inicio, meio)     # primeira metade da lista
        merge_sort(lista, meio + 1, fim)    # segunda metade da lista
        intercala(lista, inicio, meio, fim) # intercala as duas metades

