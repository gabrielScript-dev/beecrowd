# -*- coding: utf-8 -*-

PI = 3.14159
valores_in = input().split(' ')

valores_num = [float(n) for n in valores_in]

a, b, c = valores_num

area_triangulo = a * c / 2
area_circulo = PI * c ** 2
area_trapezio = (a+b)*c/2
area_quadrado = b**2
area_retangulo = a * b

print('TRIANGULO: {:.3f}'.format(area_triangulo))
print('CIRCULO: {:.3f}'.format(area_circulo))
print('TRAPEZIO: {:.3f}'.format(area_trapezio))
print('QUADRADO: {:.3f}'.format(area_quadrado))
print('RETANGULO: {:.3f}'.format(area_retangulo))