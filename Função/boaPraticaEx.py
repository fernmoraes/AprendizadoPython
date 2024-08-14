"""
DOCSTRING
- Uma docstring tem como objetivo explicar a funcionalidade de uma função.
- Uma docstring é um comentário sempre localizado na primeira linha da função.
- Uma docstring deve estar sempre entre 3 aspas dupla.
- Uma docstring contribui para a documentação de um código fonte e para seu entendimento.
"""

"""
ANOTAÇÂO DE TIPO
- Anotação de tipo (type hint) são usados para indicar os tipos de dados das variáveis
  e dos parâmetros de funções.
- O objetivo é tornar o código mais legível e organizado.
  """

def somar(a: float, b: float) -> float:
    """Esta função realiza a soma de dois números e retorna o resultado"""
    return a + b

def media(a: int, b: int, c: int) -> float:
    """Esta função realiza a média aritmética de 3 números. Retorna o resultado"""
    m = (a + b + c) / 3
    return m

somar(3, 5)
media(3, 4, 5)