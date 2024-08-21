lim = 1
numEntre = []

while lim <= 5:
    num = int(input(f'[{lim}/5] Insira um número: '))
    if 100 <= num <= 200:
        numEntre.append(num)
    lim += 1

print(f'Os números entre 100 e 200 são: {numEntre}')