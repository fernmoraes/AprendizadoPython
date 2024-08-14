def exibir_mensagem():
    print('----------------------')
    print('Bem vindo ao sistema.')
    print('----------------------')


def primo(numero):
    cont = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            cont += 1
    if cont == 2:
        print(f'Número {numero} é Primo')
    else:
        print(f'Número {numero} não é Primo')


def dobro(numero):
    d = numero * 2
    return d


# programa principal
exibir_mensagem()               # chamada da função

while True:
    print()
    print('1 - Verificar se numero é primo')
    print('2 - Calcular o dobro de um numero: ')
    print('3 - Finalizar o programa')
    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            n = int(input('Digite um numero: '))
            primo(n)            # chamada da função
        case 2:
            n = int(input('Digite um numero: '))
            d = dobro(n)        # chamada da função
            print(f'O dobro de {n} é {d}')
        case 3:
            break
        case _:
            print('Opção inválida')
