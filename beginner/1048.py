# -*- coding: utf-8 -*-

def exibir_info(salario, reajuste_ganho, em_percentual):
    
    print(f'Novo salario: {salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print(f'Em percentual: {em_percentual} %')

reajuste_salarial = {
    400 : 0.15,
    800 : 0.12,
    1200: 0.10,
    2000: 0.07,
    2000.01: 0.04
}

entrada = float(input())

for faixa in reajuste_salarial.keys():
    if entrada <= faixa or reajuste_salarial[faixa] == 0.04:
        reajuste_ganho = entrada * reajuste_salarial[faixa]
        salario = entrada + reajuste_ganho
        em_percentual = round(reajuste_salarial[faixa] * 100)
        
        exibir_info(salario, reajuste_ganho, em_percentual)
        
        break