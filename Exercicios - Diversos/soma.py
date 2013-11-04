# coding: utf-8
# Calcula uma soma de 1 até n.

n = input("Insira o numero: ")
soma = 0

for i in range(1,n+1):
    soma = soma + i
    
print soma

raw_input("Pressione qualquer tecla para continuar...")