#! /usr/bin/env python
# coding: utf-8

contador = [0, 0, 0, 0, 0, 0, 0, 0, 0]

venda_bruta = input('Insira os valores das vendas brutas dos vendedores, inserindo -1 para finalizar:\n')
while venda_bruta != -1:
    salario = int(venda_bruta*0.09) + 200
    index = (salario-200)/100
    if index > 8:
        index = 8
    contador[index] += 1
    venda_bruta = input()
    
print """\nTotal:
    - $200 ~ $299: %d
    - $300 ~ $399: %d
    - $400 ~ $499: %d
    - $500 ~ $599: %d
    - $600 ~ $699: %d
    - $700 ~ $799: %d
    - $800 ~ $899: %d
    - $900 ~ $999: %d
    - $1000 ~ ... : %d
""" % tuple(contador)