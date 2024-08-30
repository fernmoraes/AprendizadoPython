
def dados_alunos(quantidade_alunos: int) -> list:
    dados = []
    for num in range(quantidade_alunos):
        nome = input('Insira o nome do aluno: ')
        idade = int(input('Insira a idade do aluno: '))
        nota = float(input('Insira a nota do aluno: '))
        nota = float("{0:.2f}".format(nota))
        info_aluno = (nome, idade, nota)
        dados.append(info_aluno)
    return dados

def alunos_aprovados(dados: list) -> list:
    aprovados = []
    for tupla in dados:
        if tupla[-1] >= 7:
            aprovados.append(tupla[0])
    return aprovados

quantidade_alunos = int(input('Insira a quantidade de alunos: '))
dados = dados_alunos(quantidade_alunos)
aprovados = alunos_aprovados(dados)

print(aprovados)

