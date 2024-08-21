lim = 1
idadeMenor = []
idadeMaior = []

while lim <= 15:
    idade = int(input(f'[{lim}/15] Insira a idade: '))
    if idade < 18:
        idadeMenor.append(idade)
    else:
        idadeMaior.append(idade)
    lim += 1

print(f'Idades menores: {idadeMenor} | Idades maiores: {idadeMaior}')