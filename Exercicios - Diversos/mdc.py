# coding: utf-8
# Programa que calcula o MDC entre dois números.

num1 = input("Insira o menor numero: ")
num2 = input("Insira o maior numero: ")

temp = 1

for i in range(2, num1 + 1):
    if num1%i == 0 and num2%i == 0:
        temp = i

print temp

raw_input("Pressione qualquer tecla para continuar...")

