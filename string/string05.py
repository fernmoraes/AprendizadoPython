def conta_palavras(texto: str) -> int:
    """Retorne a quantidade de palavras da string"""
    lista = texto.split(' ')
    return len(lista)

texto = input('Texto: ')
print(conta_palavras(texto))