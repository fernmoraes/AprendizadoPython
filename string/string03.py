def conta_vogais(texto: str) -> int:
    """Retorna a quantidade de vogais existentes em uma string"""
    # return texto.count('a') + texto.count('e') + texto.count('i') + texto.count('o') + texto.count('u')
    cont = 0
    vogais = 'aeiou'
    for caracter in texto:
        if caracter.lower() in vogais:
            cont += 1
    return cont

texto = input('Digite o Texto: ')
quantidade = conta_vogais(texto)
print(f'Quantidade de vogais: {quantidade}')