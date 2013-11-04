#!/usr/bin/env python
# coding: utf-8

import sys
from numpy import *

def main():
    matriz_coeficientes = matrix(raw_input("Insira a matriz de coeficientes:"))
    matriz_valores = matrix(raw_input("Insira a matriz de valores"))
    matriz_solucao = matriz_coeficientes**-1 * matriz_valores
    
    print "A matriz solução é:\n", matriz_solucao

if __name__ == "__main__":
    main()
