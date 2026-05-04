# -*- coding: utf-8 -*-

num_in = float(input())

out = 'Intervalo '

if num_in >= 0 and num_in <= 25:
    out += '[0,25]'
elif num_in >= 25 and num_in <= 50:
    out += '(25,50]'
elif num_in >= 50 and num_in <= 75:
    out += '(50,75]'
elif num_in >= 75 and num_in <= 100:
    out += '(75,100]'
else:
    out = 'Fora de intervalo'

print(out)