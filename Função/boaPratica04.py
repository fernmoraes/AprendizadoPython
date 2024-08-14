def media(n1: int, n2: int, n3: int) -> float:
    """Retorna a média aritmética de 3 números"""
    resultado = (n1 + n2 + n3) / 3
    return resultado

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

print(media(a,b,c))