# -*- coding: utf-8 -*-

tabela_de_preco = {1: 4.0, 2: 4.50, 3: 5.0, 4: 2.0, 5: 1.50}

entrada = input().split(' ')

cod, qtd = [int(n) for n in entrada]

total = tabela_de_preco[cod] * qtd

print(f'Total: R$ {total:.2f}')