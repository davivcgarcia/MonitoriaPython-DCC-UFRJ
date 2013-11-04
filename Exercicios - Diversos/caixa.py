# coding: utf-8
# Exercício do caixa eletronico. Calcula quantidade de notas necessarias para um valor.

valor = input("Favor inserir o valor: ")

notas_100 = valor//100
valor = valor - notas_100 * 100

notas_50 = valor//50
valor = valor - notas_50 * 50

notas_10 = valor//10
valor = valor - notas_10 * 10

notas_5 = valor//5
valor = valor - notas_5 * 5

notas_1 = valor

print """
As quantidades sao:
    - notas de R$100: %d
    - notas de R$50: %d
    - notas de R$10: %d
    - notas de R$5: %d
    - notas de R$1: %d
""" % (notas_100, notas_50, notas_10, notas_5, notas_1)

raw_input("Pressione qualquer tecla para continuar...")