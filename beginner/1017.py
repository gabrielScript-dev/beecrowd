# -*- coding: utf-8 -*-

tempo = int(input())
velocidade = int(input())

distancia = velocidade * tempo
qtd_combustivel = distancia / 12

print('{:.3f}'.format(qtd_combustivel))