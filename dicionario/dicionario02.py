notas = {}
while True:
    rm = input('DIgite o RM: ')
    if rm == '':
        break
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    lista = [n1, n2, n3]
    notas[rm] = lista
print(notas)
print()