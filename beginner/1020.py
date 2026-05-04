# -*- coding: utf-8 -*-

dias = int(input())

ano, resto = divmod(dias, 365)
mes, dias = divmod(resto, 30)

out = '{} ano(s)\n{} mes(es)\n{} dia(s)'.format(ano, mes, dias)

print(out)
