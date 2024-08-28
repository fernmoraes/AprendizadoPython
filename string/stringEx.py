# STRING - Lista de caracteres

textoEx = 'exemplo de texto'

print(textoEx[0])
print(textoEx[4])
print()

for c in textoEx:
    print(c)

print()

# UPPER - retorna uma copia da stringem maiúscula
textoMa = textoEx.upper()
print(textoEx)
print(textoMa)
print()

# lower - retorna uma cópia da string em minúsculo
textoEx2 = 'ExEmplO De TeXtO'
textoMi = textoEx2.lower()
print(textoEx2)
print(textoMi)
print()

# title - retorna uma cópia da string com as iniciais de cada palavra em maiúsculo
textoTi = textoEx.title()
print(textoTi)
print()

# capitalize - retorna uma cópia da string com a primeira letra em maiúsculo
textoCap = textoEx.capitalize()
print(textoCap)
print()

# strip - remove os espaços brancos do inicio e do fim da string
textoEx3 = '    exemplo de texto       '
textoStr = textoEx3.strip()
print(textoEx3)
print(textoStr)
print()

# replace - substitui uma substring por outra substring
textoRe1 = textoEx.replace('e', 'X')
textoRe2 = textoEx.replace('texto', 'laranja')
print(textoRe1)
print(textoRe2)
print()

# in - verifica se uma substring está contida em uma string
if 'x' in textoEx:
    print('Achou')
else:
    print('Não achou')

if 'texto' in textoEx:
    print('Achou')
else:
    print('Não achou')

if 'batata' in textoEx:
    print('Achou')
else:
    print('Não achou')

print()

# find - verifica se uma substring está contida em uma string e retorna o indice
n1 = textoEx.find('de')
print(n1)

n2 = textoEx.find('cenoura')
print(n2)

