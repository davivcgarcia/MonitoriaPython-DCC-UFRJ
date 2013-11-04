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
# Data: 26/01/2009
# Objetivo: Realizar estatísticas de um texto.
#

def main():
    nome_do_arquivo = raw_input("Nome do arquivo: ")
    
    try:
        texto = open(nome_do_arquivo)
    except:
        print "Erro ao abrir o arquivo."

    texto = texto.read()
    
    total_caracteres = len(list(texto))
    total_linhas = len(texto.split("\n"))
    palavras = [palavra for palavra in texto.replace("\n", "").split(" ") if palavra]
    maior_palavra = ""
    frequencia_palavras = {}
    palavra_mais_frequente = ("",0)

    for palavra in palavras:
        try:
            frequencia_palavras[palavra] += 1
        except:
            frequencia_palavras[palavra] = 1
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
    
    for palavra in frequencia_palavras:
        if frequencia_palavras[palavra] > palavra_mais_frequente[1]:
            palavra_mais_frequente = (palavra,frequencia_palavras[palavra])
    
    print """Estatísticas:
    Total Caracteres: %d
    Total Linhas: %d
    Total Palavras: %d
    Maior Palavra: %s
    Palavra mais frequente: %s (%dx) """ % (total_caracteres, total_linhas, len(palavras), 
                                            maior_palavra, palavra_mais_frequente[0], 
                                            palavra_mais_frequente[1]                     )

if __name__ == "__main__":
    main()

