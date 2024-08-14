def somar(a: int, b: int) -> int:
    """Esta função soma dois números"""
    c = a + b
    return c

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))

c = somar(a, b)
print(f'soma é {c}')