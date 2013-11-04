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
# Objetivo: Verificar de a palavra A é sub-sequência da palavra B.
#

def main():
    palavra1 = raw_input("Insira as palavras (palavra1,palavra2): ")
    
    palavra1, palavra2 = palavra1.split(",")
    palavra1 = list(palavra1)
    palavra2 = list(palavra2)
    
    while palavra2 and palavra1:
        if palavra1[0] == palavra2[0]:
            palavra1.pop(0)
            palavra2.pop(0)
        else:
            palavra2.pop(0)
    
    if not palavra1:
        print("É sub-sequência.")
    else:
        print("Não é sub-sequência.")

if __name__ == "__main__":
    main()
