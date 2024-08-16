num = int(input('Digite um número: '))
div = 0

for i in range(1, num, 1):
    if num % i == 0:
        div += 1

if div == 1:
    print(f'{num} é um número primo!')
else:
    print(f'{num} não é um número primo.')