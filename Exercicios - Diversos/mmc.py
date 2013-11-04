# coding: utf-8
# Programa que calcula o MMC de uma lista de números.

lista_numeros = input("Insira os numeros (separados por virgulas): " )

mdc = 1
contador = 2
lista_numeros = list(lista_numeros)
limite = max(lista_numeros)

while contador <= limite:
    repeticao = False
    inserido = False
    print "Divisor atual: %d | Lista de numeros: %s" % (contador,lista_numeros)
    for index in range(0, len(lista_numeros)):
        if lista_numeros[index] % contador == 0:
            lista_numeros[index] = lista_numeros[index] / contador
            if not inserido:
                mdc *= contador
                inserido = True
            repeticao = True
    if not repeticao:
        contador += 1

print "MDC = %d" % mdc
