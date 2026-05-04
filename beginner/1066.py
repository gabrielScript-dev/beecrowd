# -*- coding: utf-8 -*-

entrada = []

for i in range(5):
    entrada.append(int(input()))
    
    
categoria = {
    "par(es)": 0,
    "impar(es)": 0,
    "positivo(s)": 0,
    "negativo(s)": 0
}


for n in entrada:
    if n > 0:
        categoria['positivo(s)'] += 1
    elif n < 0:
        categoria['negativo(s)'] += 1
        
    if n % 2 == 0:
        categoria['par(es)'] += 1
    else:
        categoria['impar(es)'] += 1
        
chaves = categoria.keys()

for chave in chaves:
    print(f'{categoria[chave]} valor(es) {chave}')