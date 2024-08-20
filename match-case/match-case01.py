valor_prod = float(input('Insira o valor do produto: '))

while True:
    print('''1 - Cliente Comum \n2 - Funcionário \n3 - VIP''')
    categoria = int(input('Insira sua categoria: '))

    match categoria:
        case 1:
            print(f'O valor do seu produto é de: R${valor_prod}')
            break
        case 2:
            print(f'O valor do seu produto é: R${valor_prod * 0.9}')
            break
        case 3:
            print(f'O valor do seu produto é: R${valor_prod * 0.95}')
            break
        case _:
            print('Inválido')