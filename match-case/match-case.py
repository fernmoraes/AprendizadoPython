# CALCULADORA (soma, subtração, multiplicação, divisão)

a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))

print(''' 1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão''')
opcao = int(input('Escolha uma das opções acima: '))

match opcao:
    case 1:
        print(f'Resultado da soma: {a + b}')
    case 2:
        print(f'Resultado da subtração: {a - b}')
    case 3:
        print(f'Resultado da multiplicação: {a * b}')
    case 4:
        if b != 0:
            print(f'Resultado da divisão: {a / b}')
        else:
            print('ERRO. Não é possivel fazer uma divisão por zero')
    case _:
        print('Opção inválida')
