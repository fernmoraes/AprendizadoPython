vogais = {}
aConta = 0
eConta = 0
iConta = 0
oConta = 0
uConta = 0

frase = input("Insira um texto: ")
frase = frase.lower()

for letra in frase:
    if letra == "a":
        aConta += 1
    if letra == "e":
        eConta += 1
    if letra == "i":
        iConta += 1
    if letra == "o":
        oConta += 1
    if letra == "u":
        uConta += 1

vogais['a'] = aConta
vogais['e'] = eConta
vogais['i'] = iConta
vogais['o'] = oConta
vogais['u'] = uConta

print(vogais)
