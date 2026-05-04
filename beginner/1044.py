# -*- coding: utf-8 -*-

entrada = input().split(' ')

a, b = [int(n) for n in entrada]

if a % b == 0 or b % a == 0:
    out = 'Sao Multiplos'
else:
    out = 'Nao sao Multiplos'

print(out)