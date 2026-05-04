# -*- coding: utf-8 -*-

entrada = input().split(' ')

hora_inicial, minuto_inicial, hora_final, minuto_final = [int(n) for n in entrada]

tempo_inicial = 60 * hora_inicial + minuto_inicial
tempo_final = 60 * hora_final + minuto_final

if tempo_inicial < tempo_final:
    delta = tempo_final - tempo_inicial    
else:
    delta = 24*60 - tempo_inicial + tempo_final


hora = delta // 60
delta %= 60

minuto = delta

print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')