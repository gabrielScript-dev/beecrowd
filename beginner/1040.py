# -*- coding: utf-8 -*-

def media_simples(lista: list):
    return sum(lista) / len(lista)

def media_ponderada(lista: list):
    
    soma = 0
    soma_pesos = 0

    for i in lista:
        nota, peso = i

        soma += nota * peso
        soma_pesos += peso

    media = soma / soma_pesos

    return media

def verificar_nota(nota: float):
    if nota >= 7:
        return ('Aluno aprovado.', 1)
    elif nota <= 6.9 and nota >= 5:
        return ('Aluno em exame.', 2)
    else:
        return ('Aluno reprovado.', 3)

entrada = input().split(' ')

notas = [float(n) for n in entrada]
pesos = [2, 3, 4, 1]

notas_e_pesos = list(zip(notas, pesos))

media = media_ponderada(notas_e_pesos)

print(f'Media: {media:.1f}')

msg, status = verificar_nota(media)

print(msg)

if status == 2:
    nota_exame = float(input())

    print(f'Nota do exame: {nota_exame:.1f}')

    media = media_simples([nota_exame, media])

    if media >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print(f'Media final: {media:.1f}')