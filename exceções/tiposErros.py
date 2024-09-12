'''
    Tipos de erros:
-Erros de sintaxe
-Exceções 
'''

'''
    Erros de sintaxe:
Erro causado pela sintaxe errada
Provoca encerramento do programa

Ex:
falta de dois-pontos ":"
'''

'''
    Exceções:
Exceções ocorrem quando o programa está sintaticamente correto, mas ocódigo resulta em um erro
São erros ocorridos em tempo de execução
Uma exceção interrompe a execução do programa

Ex:
Executar uma divisão por zero

Tipos de exceções:
-TypeError: Quando uma operação ou função é aplicada a um objeto do tipo errado,
como adicionar uma string a um inteiro
-NameError: Quando o nome de variácel ou função não pe encontrado no escopo atual
-ValueError: Quando uma função ou método é chamado com um parâmentro ou entrada inválido,
como tentar converter uma string em um inteiro quando a string não representa um número válido
-ZeroDivisionError: quando é feita uma tentativa de dividir um número por 0
'''

'''
    Try e Except
-Try: Instruções que podem gerar exceções
-Except: Instruções que lidam com as exceções
'''

try:
    x = 5
    y = "hello"
    z = x+y
except TypeError:
    print('Ocorreu um erro')

try:
    a = int(input('Informe um número: '))
    b = int(input('Informe um número: '))
    c = a/b
    print(c)
except ZeroDivisionError:
    print('Não é possível fazer uma divisão por zero')
except ValueError:
    print('Ovalor informado não é um numero inteiro')
except Exception:   #Pode tratar qualquer erro genêrico com Exception
    print('Ocorreu um erro')
else:               #Caso não ocorra nenhuma exceção
    print('Operação realizada com sucesso')
finally:            #Finally ocorre tendo exceção ou não
    print('Fim da conta')

