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
# Objetivo: Verificar se uma palavra é palíndroma.
#

def main():
    palavra = raw_input("Insira uma palavra: ")
    
    palavra = list(palavra)
    palavra_ao_contrario = palavra + []
    palavra_ao_contrario.reverse()

    if palavra == palavra_ao_contrario:
        print "É palíndromo !"
    else:
        print "Não é palíndromo !"
    return 0

if __name__ == "__main__":
    main()
