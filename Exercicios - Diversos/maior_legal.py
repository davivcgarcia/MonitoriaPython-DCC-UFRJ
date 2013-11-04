#!/usr/bin/env python
# coding: utf-8

lista_de_numeros = []
quantidade = input("Quantidade de números: ")

# Nesse loop estou realizando a leitura dos N dados e inserindo na lista.
print "Insira os números, um por linha:"
for contador in range(0,quantidade):
    lista_de_numeros = lista_de_numeros +[input()]

# Esse comando funciona <uma lista qualquer>.sort() e ordena os elementos da lista.
lista_de_numeros.sort()

#Imprimo o maior, ou seja, o último elemento (indexado pelo -1).
print "\nO maior elemento é:", lista_de_numeros[-1]

raw_input("Pressione qualquer tecla para continuar...")
