'''
    Gerando Exceções
-raise: raise permite forçar a ocorrência de uma exceção específica
'''

try:
    raise NameError         # Gera uma exceção
except NameError:
    print ('Ocorreu uma exceção')

try:
    a = int(input('Informe um número: '))
    b = int(input('Informe um número: '))
    c = a/b
    if a < 0 or b < 0:
        raise TypeError     # Gera exceção se o numero for negativo
    print(c)
except ZeroDivisionError:
    print('Não é possível fazer uma divisão por zero')
except ValueError:
    print('Ovalor informado não é um numero inteiro')
except TypeError:
    print('O número é negativo')
else:
    print('Operação realizada com sucesso')
finally:
    print('Fim da conta')