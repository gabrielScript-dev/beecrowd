# -*- coding: utf-8 -*-

notas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0]

n = int(input())

eh_valido = n > 0 and n < 1000000

if eh_valido:
    
    print(n)
    for nota in notas:
        qtd_de_notas = int(n // nota)
        n %= nota
        
        out = '{} nota(s) de R$ {:.2f}'.format(qtd_de_notas, nota)
        out = out.replace('.',',')
        
        print(out)