def calcular_salario(salario: float) -> float:
    """Verifica se o salário é maior que 2000 para 7% a mais, senão 15% a mais. Retorna reajuste"""
    if salario > 2000:
        reajuste = salario + (salario * 0.07)
    else:
        reajuste = salario + (salario * 0.15)
    return reajuste

a = float(input('Insira seu salário: '))
aumento = calcular_salario(a)

if a > 2000:
    bonus = '7%'
else:
    bonus = '15%'

print(f'Seu salário teve um aumento de {bonus} e agora é R${aumento}')
