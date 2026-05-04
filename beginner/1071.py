# -*- coding: utf-8 -*-

from functools import reduce

x = int(input())
y = int(input())

if x == y:
    soma = 0
else:
    valores = list(range(min(x,y)+1,max(x,y)))
    valores_impares = list(filter(lambda x: x % 2 != 0, valores))

    soma = reduce(lambda x,y: x+y, valores_impares)

print(soma)