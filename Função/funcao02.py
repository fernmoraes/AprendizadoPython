def forma(lados):
    if lados == 3:
        print("triângulo")
    elif lados == 4:
        print("Quadrilátero")
    elif lados == 5:
        print("Pentágono")
    else:
        print("Valor inválido")

lados = int(input("Insira o número de lados: "))
forma(lados)