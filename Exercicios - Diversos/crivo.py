# coding: utf-8
# Esse algorítimo é conhecido como Crivo de Eratóstenes.
# http://www.educ.fc.ul.pt/icm/icm2001/icm31/crivo.htm

quantidade = input("Insira a quantidade de primos: ")

lista = [True] * quantidade # Cria uma lista com N elementos True.

for fator in range(2,quantidade):
    for i in range(fator*2,quantidade,fator):
        lista[i] = False

for i in range(2,len(lista)):
    if lista[i]:
        print i,

raw_input("\nPressione qualquer tecla para continuar...")
