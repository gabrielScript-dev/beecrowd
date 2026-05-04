# -*- coding: utf-8 -*-

class Funcionario:
    def __init__(self, numero, horas_trabalhadas, valor_hora):
        self.__numero = numero
        self.__horas_trabalhadas = horas_trabalhadas
        self.__valor_hora = valor_hora

    def salary(self):
        return self.__valor_hora * self.__horas_trabalhadas
    
    def __repr__(self):
        return 'NUMBER = {}\nSALARY = U$ {:.2f}'.format(self.__numero, self.salary())
    
numero = int(input())
horas = int(input())
valor_hora = float(input())

funcionario = Funcionario(numero, horas, valor_hora)

print(funcionario.__repr__())