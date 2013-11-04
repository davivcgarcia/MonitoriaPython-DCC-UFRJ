#!/usr/bin/env python
# coding: utf-8

maior_numero = 0 # Começa em 0 pra ser menor que qualquer um.
quantidade = input("Quantidade de números: ")

# Nesse loop eu vou lendo os números e comparando com o maior ja lido.
print "Insira os números, um por linha:"
for contador in range(0,quantidade):
    numero_lido = input()
    if numero_lido > maior_numero:
        maior_numero = numero_lido

print "O maior_numero é: ", maior_numero

raw_input("Pressione qualquer tecla para continuar...")
