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
# Objetivo: Verificar se uma frase é palíndroma.
#

def main():
    frase = raw_input("Insira uma frase: ")
    
    frase = frase.lower()
    frase = [char for char in frase if char != ' ']
    frase_ao_contrario = frase + []
    frase_ao_contrario.reverse()

    if frase == frase_ao_contrario:
        print "É uma frase palíndroma !"
    else:
        print "Não é uma frase palíndroma !"
    return 0

if __name__ == "__main__":
    main()
