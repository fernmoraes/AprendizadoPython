lim = 1
numLista = []

while lim <= 10:
    num = int(input(f'[{lim}/10]Insira um número: '))
    numLista.append(num * 2)
    lim += 1

print(numLista)