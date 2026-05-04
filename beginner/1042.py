# -*- coding: utf-8 -*-

def imprimir(lista: list):
    for n in lista:
        print(n)

entrada = input().split(' ')

valores = [int(n) for n in entrada]
valores_ordenados = sorted(valores)

imprimir(valores_ordenados)
print()
imprimir(valores)