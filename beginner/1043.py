# -*- coding: utf-8 -*-

entrada = input().split(' ')

a,b,c = [float(n) for n in entrada]

if a + b > c and a + c > b and b + c > a:
    out = 'Perimetro ='
    calc = a+b+c
else:
    out = 'Area ='
    calc = (a+b)*c/2
    
print(out, f'{calc:.1f}')