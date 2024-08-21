num = None
numLista = []
lim = 0

while num != 0:
    num = int(input(f'Insira (0) para finalizar | Você já inseriu {lim} números | Insira um número: '))
    numLista.append(num)
    lim += 1

soma = sum(numLista)

print(f'A soma dos números inseridos é: {soma}')