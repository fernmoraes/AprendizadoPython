n = int(input('Digite um número: '))
fat = 1

for i in range(1, n + 1, 1):
    fat *= i

print(f'Fatorial de {n}: {fat}')
