# coding: utf-8
# Verifica se um número e primo.

numero = input("Insira o numero: ")
primo = True

for i in range(2,numero):
    if numero % i == 0:
        primo = False

if primo:
    print "E primo !"
else:
    print "Nao e primo !"

raw_input("Pressione qualquer tecla para continuar...")