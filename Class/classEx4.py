lista_de_alunos = []

class Infos_Alunos:
    def __init__(self, aluno, idade, nota):
        self.aluno = aluno
        self.idade = idade
        self.nota = nota
    
    def exibir_informacoes(self):
        print(f'Aluno: {self.aluno}, Idade: {self.idade}, Nota Final: {self.nota}')


quantidade = int(input('Quantos alunos você quer registrar?: '))

for i in range(quantidade):
    aluno = input(f'Nome do aluno {i+1}: ')
    idade = int(input(f'Idade do aluno {i+1}: '))
    nota = float(input(f'Nota do aluno {i+1}: '))
    novo_aluno = Infos_Alunos(aluno, idade, nota)
    lista_de_alunos.append(novo_aluno)

print("\nAlunos cadastrados:")
for aluno in lista_de_alunos:
    aluno.exibir_informacoes()