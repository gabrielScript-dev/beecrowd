# -*- coding: utf-8 -*-

entrada = float(input())

faixas = [
        (0, 2000, 0.00),
        (2000, 3000, 0.08),
        (3000, 4500, 0.18),
        (4500, float('inf'), 0.28)
    ]

imposto = 0.0

if entrada < 2000.0:
    print('Isento')
else:
    for minimo, maximo, taxa in faixas:
        if entrada > minimo:
            valor_faixa = min(entrada, maximo) - minimo
            imposto += valor_faixa * taxa


    print(f'R$ {imposto:.2f}')