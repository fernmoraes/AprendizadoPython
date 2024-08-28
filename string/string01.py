def conta_caracteres(frase: str) -> int:
    """Retorna a quantidade de caracteres de uma string."""
    return len(frase)

frase = input('Digite um texto: ')
quantidade = conta_caracteres(frase)
print(quantidade)