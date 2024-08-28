def lista_palavras(texto: str) -> list:
    """Retorne uma lista com as palavras da string"""
    lista = texto.split(' ')
    return lista

texto = input('Texto: ')
print(lista_palavras(texto))