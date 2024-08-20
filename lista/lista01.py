pares = []
impares = []

for i in range(10):
    numero = int(input('Numero: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)
