# -*- coding: utf-8 -*-

def classifica_angulo(a, b, c):
    if a**2 == b**2 + c**2:
        return 'TRIANGULO RETANGULO'
    if a**2 > b**2 + c**2:
        return 'TRIANGULO OBTUSANGULO'
    return 'TRIANGULO ACUTANGULO'

def classifica_lados(a, b, c):
    if a == b == c:
        return 'TRIANGULO EQUILATERO'
    if a == b or b == c or a == c:
        return 'TRIANGULO ISOSCELES'
    return ''

entrada = input().split(' ')

a, b, c = sorted([float(n) for n in entrada], reverse=True)

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    resultado = []
    resultado.append(classifica_angulo(a, b, c))
    if classificacao := classifica_lados(a, b, c):
        resultado.append(classificacao)
    print('\n'.join(resultado))