def peso_conta(altura, genero):
    if genero == "m":
        peso = (72.7 * altura) - 58
    elif genero == "f":
        peso = (62.1 * altura) - 44.7
    return peso


altura = float(input('Insira sua altura: '))
genero = input('insira seu genero | M ou F: ').lower()

peso_resultado = peso_conta(altura, genero)

print(f'O seu peso ideal sendo do gênero {genero} e tendo a altura {altura} é de {peso_resultado}kg')