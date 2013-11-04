#! /usr/bin/env python
# coding: utf-8
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Autor: Davi Vercillo C. Garcia 
# Data: 24/01/2009
# Objetivo: Determinar a fatoração de um número dado.
#

def main():
    numero = input("Insira o número: ")
    contador = 2
    divisores = {}
    
    while contador <= numero:
        if numero%contador == 0:
            try:
                divisores[contador] += 1
            except:
                divisores[contador] = 1
            numero = numero/contador
            continue
        contador += 1
    
    print "A fatoração é", str(divisores)[1:-1].replace(": ","^").replace(", ", " x ")
    return 0

if __name__ == "__main__":
    main()
