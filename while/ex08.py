lista = []
cont = 0
lim = 1

while lim <= 10:
    num = int(input(f'[{cont}/10]Insira um número:'))
    lista.append(num)
    cont += 1
    lim += 1

lista.sort()
menorNumero = lista[0]
print(f'O menor número da lista é: {menorNumero}')
