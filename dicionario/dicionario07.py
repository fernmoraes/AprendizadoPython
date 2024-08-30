palavras = {}
frase = input('Digite uma frase: ')
lista = frase.split()                           # Divide a frase em palavras e salva na lista

for palavra in lista:                           # Pega cada palavra na lista
    palavras[palavra] = frase.count(palavra)    # Salva cada palavra no dicionário 'palavras'. Então verifica se existe a palavra na frase

print(palavras)

