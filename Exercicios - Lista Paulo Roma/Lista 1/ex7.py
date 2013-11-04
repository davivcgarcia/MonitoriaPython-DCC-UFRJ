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
# Objetivo: Verificar se uma palavra é palíndroma da outra ou se são anagramas.
#

def main():
    palavra1 = raw_input("Insira as palavra (palavra1,palavra2): ")

    palavra1,palavra2 = palavra1.split(",")
    
    palavra1 = [char for char in palavra1]
    palavra2 = [char for char in palavra2]
    palavra2.reverse()

    if palavra1 == palavra2:
        print "É palíndromo mútuo !"
        return 0
    else:
        for char1 in palavra1:
            if not char1 in palavra2:
                print "Não é nem palíndromo mútuo nem anagrama !"
                return 0
        print "Não é palíndromo mútuo mas é anagrama !"
        return 0

if __name__ == "__main__":
    main()
