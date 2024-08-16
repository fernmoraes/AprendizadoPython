quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))
quantidade_notas = int(input("Digite a quantidade de notas por aluno: "))

# Loop para cada aluno
for aluno in range(1, quantidade_alunos + 1):
    soma_notas = 0
    # Solicita as notas do aluno
    print(f"Notas do aluno {aluno}:")
    for nota_numero in range(1, quantidade_notas + 1):
        nota = float(input(f"Digite a nota {nota_numero}: "))
        soma_notas += nota
    # Calcula a média
    media = soma_notas / quantidade_notas
    # Exibe a média do aluno
    print(f"A média do aluno {aluno} é: {media}")