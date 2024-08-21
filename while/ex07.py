print('Insira dois números diferentes')
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))

while num1 == num2:
    print('Os números não podem ser iguais')
    print('-------------------------------')
    print('Insira dois números diferentes')
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))

dif = num1 - num2
dif = abs(dif) # (abs) transforma um número negativo em positivo
print(f'A diferença é {dif}')