# -*- coding: utf-8 -*-

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

n = float(input())
eh_valido = n >= 0 and n <= 1000000.00

if eh_valido:
    valor_em_centavos = int(round(n * 100))

    print('NOTAS:')
    for nota in notas:
        qtd_de_notas = valor_em_centavos // nota
        valor_em_centavos %= nota
        print(f'{qtd_de_notas} nota(s) de R$ {nota / 100:.2f}')

    print('MOEDAS:')
    for moeda in moedas:
        qtd_de_moedas = valor_em_centavos // moeda
        valor_em_centavos %= moeda
        print(f'{qtd_de_moedas} moeda(s) de R$ {moeda / 100:.2f}')
