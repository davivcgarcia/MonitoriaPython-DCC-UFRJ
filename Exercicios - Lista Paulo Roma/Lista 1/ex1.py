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
# Objetivo: Verificar se um dado número é um número perfeito (soma dos seus
#           divisores é igual a ele mesmo).
#

def main():
    numero = input("Insira o número: ")
    contador = 1
    soma_dos_divisores = 0

    while contador < numero:
        if numero%contador == 0:
            soma_dos_divisores += contador
        contador += 1

    if numero == soma_dos_divisores:
        print "O número", numero, "é um número mágico !"
    else:
        print "O número", numero, "não é um número mágico !"

    return 0

if __name__ == "__main__":
    main()
