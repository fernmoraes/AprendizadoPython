dados = {}

for n in range(5):
    rm = input('Insira o RM do aluno: ')
    n1 = float(input('Insira a primeira nota: '))
    n2 = float(input('Insira a segunda nota: '))
    n3 = float(input('Insira a terceira nota: '))
    lista = [n1, n2, n3]
    dados[rm] = lista

print(dados)

for rm, nota in dados.items():
    n1 = nota[0]
    n2 = nota[1]
    n3 = nota[2]
    media = (n1 + n2 + n3)/3
    media = float("{0:.2f}".format(media))          # Arredonda a média para duas casa decimais  
    print(f'O aluno com RM {rm} possui média {media}')