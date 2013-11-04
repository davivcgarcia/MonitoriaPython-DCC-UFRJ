#! /usr/bin/env python
# coding: utf-8

notas_lidas = []

nota = input('Insira notas, uma por vez, inserindo -1 para finalizar:\n')
while nota != -1:
    notas_lidas += [nota]
    nota = input()

notas_invertidas = notas_lidas[::-1]
total = len(notas_lidas)
soma = sum(notas_lidas)
media = float(soma)/total

valores_acima = []
valores_abaixo = []
for nota in notas_lidas:
    if nota > media:
        valores_acima += [nota]
    elif nota < media:
        valores_abaixo += [nota]
total_valores_acima = len(valores_acima)
total_valores_abaixo = len(valores_abaixo)
    
print """\nResultados:
    - Total lido: %s
    - Valores lidos: %s
    - Valores lidos (ordem inversa): %s
    - Soma: %s
    - Média: %s
    - Valores acima da média: %s (Total: %s)
    - Valores abaixo da média: %s (Total: %s)
    
Programa finalizado... """ % (total, notas_lidas, notas_invertidas, soma, media, valores_acima, total_valores_acima, valores_abaixo, total_valores_abaixo)