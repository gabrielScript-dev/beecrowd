# -*- coding: utf-8 -*-

coordenada_ponto_1 = input().split(' ')
coordenada_ponto_2 = input().split(' ')

coordenada_ponto_1 = [float(n) for n in coordenada_ponto_1]
coordenada_ponto_2 = [float(n) for n in coordenada_ponto_2]

x1, y1 = coordenada_ponto_1
x2, y2 = coordenada_ponto_2

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print('{:.4f}'.format(distancia))