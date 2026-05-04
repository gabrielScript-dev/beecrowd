# -*- coding: utf-8 -*-

notas = []
pesos = [2, 3, 5]

for i in range(3):
    nota = float(input())

    notas.append(nota)

soma = 0
for index, nota in enumerate(notas):

    soma += nota * pesos[index]

media = soma / sum(pesos)

print('MEDIA = {:.1f}'.format(media))