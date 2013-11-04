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
# Data: 25/01/2009
# Objetivo: Realizar conversão de números decimais para números romanos.
#

def main():
    numero_arabico = input("Insira o número a ser convertido: ")
    numero_romano = ''
    contador = 0
    
    valor_arabico = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    algarismos_romanos = ["M", "CM", "D", "CD", "C", "XC",
                          "L", "XL", "X", "IX", "V", "IV",
                          "I"                             ]
    
    while numero_arabico:
        if numero_arabico-valor_arabico[contador] >= 0:
            numero_arabico -= valor_arabico[contador]
            numero_romano += algarismos_romanos[contador]
            continue
        contador += 1
    
    print "A conversão é", numero_romano,"."

if __name__ == "__main__":
    main()

