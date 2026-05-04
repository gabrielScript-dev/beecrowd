# -*- coding: utf-8 -*-

class Funcionario:
    def __init__(self, nome, salario, vendas):
        self.__nome = nome
        self.__salario = salario
        self.__vendas = vendas

    def salary(self):
        return self.__salario + self.__vendas * 0.15
    
    def __repr__(self):
        return 'TOTAL = R$ {:.2F}'.format(self.salary())
    
nome = input()
salario = float(input())
vendas = float(input())

funcionario = Funcionario(nome=nome, salario=salario, vendas=vendas)

print(funcionario.__repr__())