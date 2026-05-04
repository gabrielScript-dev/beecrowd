# -*- coding: utf-8 -*-


valores = []

for i in range(4):
    valor = int(input())

    valores.append(valor)

a, b, c, d = valores

diferenca = a * b - c * d

print(f'DIFERENCA = {diferenca}')