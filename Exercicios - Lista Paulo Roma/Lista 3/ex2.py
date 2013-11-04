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

class Data:    
    def __init__(self, dia, mes, ano):
        if (0 <= dia <= 30) and (2 <= len(str(ano)) <= 4):
            if (type(mes) is int) and (0 <= mes <= 12):
                self.data = (dia, mes, ano)
            elif type(mes) is str and mes in ("Jan", "Fev", "Mar", "Abr", "Mai",
                                              "Jun", "Jul", "Ago", "Set", "Out",
                                              "Nov", "Dez"):
                self.data = (dia, mes, ano)
            else:
                print "Data inválida."
                self.data = ()
        else:
            print "Data inválida."
            self.data = ()
    
    def __eq__(self, data1, data2):
        pass
    
    def __str__(self):
        if type(self.data[1]) is int:
            return "%d/%d/%d" % self.data
        if type(self.data[1]) is str:
            return "%d de %s de %d" % self.data

def main():
    data = Data(12, "Jan", 21)
    print data

if __name__ == "__main__":
    main()