def remove_espacos(texto: str) -> str:
    """Remover os espaços em branco de uma string."""
    return texto.replace(" ", "")


texto = input('Digite o texto: ')
print(remove_espacos(texto))