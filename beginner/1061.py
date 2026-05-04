# -*- coding: utf-8 -*-


dia_inicial = int(input().split(' ')[1])
hora_inicial = input()

dia_final = int(input().split(' ')[1])
hora_final = input()

hora_inicial = [int(n) for n in hora_inicial.split(' : ')]
hora_final = [int(n) for n in hora_final.split(' : ')]

def tempo_total(tempo: list):
    
    hora, minuto, segundos = tempo

    return  hora*3600 + minuto*60 + segundos

tempo_inicial = tempo_total(hora_inicial)
tempo_final = tempo_total(hora_final)

if tempo_inicial < tempo_final:
    delta = tempo_final - tempo_inicial
else:
    delta = (24*3600) - tempo_inicial + tempo_final


horas = delta//3600
delta %= 3600

minutos = delta // 60
delta %= 60

segundos = delta

delta_dias = dia_final - dia_inicial

if horas < 24 and horas != 0 and delta_dias > 0:
    delta_dias -= 1

print(f'{delta_dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')