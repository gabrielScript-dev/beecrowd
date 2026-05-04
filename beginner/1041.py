# -*- coding: utf-8 -*-

def verificar_quadrante(x, y):
    if x < 0 and y > 0:
        return 'Q2'
    elif x > 0 and y > 0:
        return 'Q1'
    elif x < 0  and y < 0:
        return 'Q3'
    else: 
        return 'Q4'

entrada = input().split(' ')

x, y = [float(n) for n in entrada]

if x == 0 and y == 0:
    print('Origem')
elif x == 0 and  y != 0:
    print('Eixo Y')
elif x != 0 and y == 0:
    print('Eixo X')
else:
    quadrante = verificar_quadrante(x, y)
    
    print(quadrante)