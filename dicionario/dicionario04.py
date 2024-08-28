dados = {}

for n in range(5):
    produto = input('Insira o nome do produto: ')
    valor = float(input('Insira o valor do produto: '))
    dados[produto] = valor

for produto, valor in dados.items():
    if valor >= 50:
        print(produto, valor)

print(dados)