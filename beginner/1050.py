# -*- coding: utf-8 -*-

ddd_dict = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

entrada = int(input())

ddd_list = ddd_dict.keys()

if entrada in ddd_list:
    print(ddd_dict[entrada])
else:
    print('DDD nao cadastrado')
