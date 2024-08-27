alunos = {}
while True:
    rm = input('Informe o RM: ')
    if rm == '':
        break
    nome = input('Informe o nome: ')
    alunos[rm] = nome
print(alunos)
print()