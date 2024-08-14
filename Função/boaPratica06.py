def soma_divisores(numero: int) -> int:
    """Calcula o somatório dos divisores de um número inteiro"""
    divisores = []
    a = 1
    while a <= numero:
        if numero % a == 0:
            divisores.append (a)
        a += 1
    resultado = sum(divisores)
    
    return resultado

numero = int(input('Insira um número: '))
print(soma_divisores(numero))