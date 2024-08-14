def quadrado(a: int) -> int:
    """Retorna o número ao quadrado"""
    return a**2

a = int(input('Insira um número: '))

print(f'{a} ao quadrado é {quadrado(a)}')