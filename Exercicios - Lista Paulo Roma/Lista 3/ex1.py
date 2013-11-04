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
# Data: 28/01/2009
# Objetivo: Calcula a raiz quadrada de X, usando busca binária.
#

def raiz(x_inicial, x_final, x, erro=0.00001):
    temp = (x_inicial + x_final)/2.0
    if temp*temp > x:
        if abs(temp - (temp + x_inicial)/2) < erro:
            return temp
        return raiz(x_inicial, temp, x)
    elif temp*temp < x:
        if abs(temp - (temp + x_final)/2) < erro:
            return temp
        return raiz(temp, x_final, x)
    else:
        return temp

def main():
    x = input("Insira o número (<100): ")
    print "A raiz quadrada de", x, "é", raiz(0, x, x), "."

if __name__ == "__main__":
    main()