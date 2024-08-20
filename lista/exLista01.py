import random

cont = 1
lista = []

while cont <= 10:
    num_aleatorio = random.randint(1,20)
    lista.append(num_aleatorio)
    cont += 1

print(lista)