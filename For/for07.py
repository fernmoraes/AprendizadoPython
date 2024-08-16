num = int(input('Insira um número: '))
lista = []

for div in range(1, num):
    if num % div == 0:
        lista.append(div)

print(lista)
