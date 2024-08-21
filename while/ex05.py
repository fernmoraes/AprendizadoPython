lim = 1
numImpar = []
while lim <= 15:
    num = int(input(f'[{lim}/15] Insira um número: '))
    if num % 2 != 0:
        numImpar.append(num)
    lim += 1

soma = sum(numImpar) #O 'sum' SOMA OS NÚMEROS DENTRO DA LISTA
print(f'A soma dos números ímpares é: {soma}')