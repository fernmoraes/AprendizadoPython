def provas(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 6:
        print("Você foi aprovado")
    else:
        print("Você foi reprovado")

nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))

provas(nota1, nota2)