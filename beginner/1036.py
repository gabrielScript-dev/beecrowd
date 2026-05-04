# -*- coding: utf-8 -*-

entrada = input().split(' ')

a, b, c = [float(n) for n in entrada]

delta = b**2-4*a*c

if delta >= 0 and a > 0:
    
    raiz_1 = (-b+delta**0.5)/(2*a)
    raiz_2 = (-b-delta**0.5)/(2*a)
    
    out = f'R1 = {raiz_1:.5f}\nR2 = {raiz_2:.5f}'
    
    print(out)
else:
    print('Impossivel calcular')