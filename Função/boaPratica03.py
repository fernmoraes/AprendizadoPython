def quadrado(numero: float) -> float:
    """Retorna o quadrado de um número"""
    return numero**2

def soma_dos_quadrados(a: float, b: float) -> float:
    """Chama a função quadrado para dois números e retorna a soma deles"""
    return quadrado(a) + quadrado(b)

a = float(input('Insira o primeiro número: '))
b = float(input('Insira o segundo número: '))

resultado = soma_dos_quadrados(a, b)

print(resultado)