print('''D - Divorciado \nC - Casado \nS - Solteiro \nV - Viuvo ''')

estado = input('Qual seu estado civil: ').upper()

match estado:
    case 'D':
        print('Você é divorciado :/')
    case 'C':
        print('Você é casado :)')
    case 'S':
        print('Você é solteiro :D')
    case 'V':
        print('Você é viuvo :(')
    case _:
        print('Opção inválida')