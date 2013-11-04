# coding: utf-8
# Exercício do pintor. Calcula quantidade de latas/galoes necessárias para uma certa area.

import math

area = input("Insira a área: ")
litros = 1.1*(area/6.0)

solatas = math.ceil(litros/18)
sogaloes = math.ceil(litros/3.6)

latas = litros//18
litros = litros - latas*18
galoes = math.ceil(litros/3.6)

print """
As quantidades são:
    so latas: %d
    so galoes: %d
    latas e galoes: %d e %d
""" % (solatas, sogaloes, latas, galoes)

raw_input("Pressione qualquer tecla para continuar...")