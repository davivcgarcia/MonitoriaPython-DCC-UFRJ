# coding: utf-8
# Exerc�cio do pintor. Calcula quantidade de latas/galoes necess�rias para uma certa area.

import math

area = input("Insira a �rea: ")
litros = 1.1*(area/6.0)

solatas = math.ceil(litros/18)
sogaloes = math.ceil(litros/3.6)

latas = litros//18
litros = litros - latas*18
galoes = math.ceil(litros/3.6)

print """
As quantidades s�o:
    so latas: %d
    so galoes: %d
    latas e galoes: %d e %d
""" % (solatas, sogaloes, latas, galoes)

raw_input("Pressione qualquer tecla para continuar...")