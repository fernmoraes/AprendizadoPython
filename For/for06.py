lista = []

for cont in range (10):
    num = int(input('Insira um número: '))
    lista.append(num)

lista.sort()
menorNum = lista[0]
maiorNum = lista[10]

print(f'O menor número é {menorNum} e o maior é {maiorNum}')