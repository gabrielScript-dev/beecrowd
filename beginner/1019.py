# -*- coding: utf-8 -*-

tempo_segundos = int(input())

hora, resto = divmod(tempo_segundos, 3600)
minutos, segundos = divmod(resto, 60)

print(f"{hora}:{minutos}:{segundos}")