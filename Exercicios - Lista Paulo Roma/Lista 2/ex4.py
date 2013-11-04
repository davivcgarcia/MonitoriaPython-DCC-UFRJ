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
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Autor: Davi Vercillo C. Garcia 
# Data: 26/01/2009
# Objetivo: Programa capaz de gerenciar diagramas de palavras cruzadas.
#

def main():
    informacoes = raw_input("Insira as informações (X Y P PALAVRA):\n")
    informacoes = []+[informacoes.split(" ")]
    
    entrada = tamanho_x = tamanho_y = 1
    
    while entrada:
        entrada = raw_input()
        informacoes += [entrada.split(" ")]

    informacoes.pop(-1)

    for info in informacoes:
        temp_x = int(info[0])+len(info[3])-1
        temp_y = int(info[1])+len(info[3])-1

        if info[2] == "H" and temp_x > tamanho_x:
            tamanho_x = temp_x
        if info[2] == "V" and temp_y > tamanho_y:
            tamanho_y = temp_y

        if int(info[0]) > tamanho_x:
            tamanho_x = int(info[0])
        if int(info[1]) > tamanho_y:
            tamanho_y = int(info[1])

    print tamanho_x, tamanho_y

if __name__ == "__main__":
    main()


























