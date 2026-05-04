# -*- coding: utf-8 -*-

vertebrado = {
    'ave': {
        'carnivoro': 'aguia',
        'onivoro': 'pomba',
    },

    'mamifero': {
        'onivoro': 'homem',
        'herbivoro': 'vaca'
    }
}

invertebrado = {
    'inseto': {
        'hematofago': 'pulga',
        'herbivoro': 'lagarta'
    },

    'anelideo': {
        'hematofago':'sanguessuga',
        'onivoro': 'minhoca'
    }
}

entrada = [input() for n in range(3)]

x, y, z= entrada

if x == 'vertebrado':
    out = vertebrado[y][z]
else:
    out = invertebrado[y][z]

print(out)