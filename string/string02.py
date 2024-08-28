def converte_maiusculo(frase: str) -> str:
    """Retorna uma string com todos os caracteres em maiúsculo."""
    return frase.upper()

frase = input('Digite um texto: ')
print(converte_maiusculo(frase))
