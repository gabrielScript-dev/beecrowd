# -*- coding: utf-8 -*-

qtd_num_positivos = 0

for i in range(6):
    entrada = float(input())

    if entrada > 0:
        qtd_num_positivos += 1

print(f'{qtd_num_positivos} valores positivos')