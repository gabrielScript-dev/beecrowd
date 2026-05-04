# -*- coding: utf-8 -*-

valores_in = input().split(' ')

valores_num = [int(n) for n in valores_in]

a, b, c = valores_num

x = (a+b+abs(a-b)) / 2

maior_x_c = int((x + c + abs(x-c)) / 2)

print(maior_x_c, 'eh o maior')
