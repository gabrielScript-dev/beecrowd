# -*- coding: utf-8 -*-

entrada = input().split(' ')

valores = [ int(n) for n in entrada]

a, b, c, d = valores

out = "Valores aceitos" if b > c and d > a and (c+d) > (a+b) and (c > 0 and d > 0) and (a % 2 == 0) else "Valores nao aceitos"

print(out)