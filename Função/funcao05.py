def area_conta(raio):
    resultado = 3.14 * raio**2
    return resultado

def perimetro_conta(raio):
    resultado = 3.14 * 2 * raio
    return resultado

raio = float(input('Insira o raio do circulo: '))
area_resultado = area_conta(raio)
perimetro_resultado = round(perimetro_conta(raio))

print(f'O raio é {raio}m, a área é {area_resultado}m², o perímetro é {perimetro_resultado}m')