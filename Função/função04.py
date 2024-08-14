def par_impar(num):
    if num % 2 == 0:
        valor = True
    else:
        valor = False
    return valor

num = int(input('Insira seu número: '))

res = par_impar(num)

if res == True:
    print('Par')

elif res == False:
    print('Impar')