# -*- coding: utf-8 -*-

entrada = input().split(' ')

tempo_inicial, tempo_final = [int(n) for n in entrada]

if tempo_inicial < tempo_final:
    delta = tempo_final - tempo_inicial
else:
    delta = 24 - tempo_inicial + tempo_final

print(f'O JOGO DUROU {delta} HORA(S)')