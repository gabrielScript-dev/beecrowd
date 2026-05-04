# -*- coding: utf-8 -*-

soma = 0
qtd_num_positivos = 0

for i in range(6):
    entrada = float(input())

    if entrada > 0:
        qtd_num_positivos += 1
        soma += entrada

media = soma / qtd_num_positivos

print(f'{qtd_num_positivos} valores positivos')
print(f'{media:.2n}')