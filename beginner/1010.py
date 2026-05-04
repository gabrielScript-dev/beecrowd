# -*- coding: utf-8 -*-

total = 0
for i in range(2):
    cod, qtd, valor_uni = input().split(' ')

    qtd = int(qtd)
    valor_uni = float(valor_uni)

    total += qtd * valor_uni

print('VALOR A PAGAR: R$ {:.2f}'.format(total))