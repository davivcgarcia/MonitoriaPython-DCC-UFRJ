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
# Objetivo: Modelar um sistema de contas de cliente de um banco.
#

clientes = {}

def adiciona_cliente(nome):
    clientes[nome] = {}

def adiciona_conta(nome):
    if nome in clientes:
        try:
            numero_conta = len(clientes[nome])
            clientes[nome][numero_conta] = ["", 0.0]
            return numero_conta
        except:
            clientes[nome][0] = ["", 0.0]
            return 0
    else:
        print "Erro: Nome de cliente inválido."

def realizar_lancamento(nome, conta, valor):
    if nome in clientes and conta in clientes[nome]:
        clientes[nome][conta][1] += valor
        clientes[nome][conta][0] += "L: %s\n" % valor
    else:
        print "Erro: Nome de cliente e/ou número de conta inválido."

def realizar_extrato(nome, conta):
    if nome in clientes and conta in clientes[nome]:
        print clientes[nome][conta][0]
    else:
        print "Erro: Nome de cliente e/ou número de conta inválido."

def verificar_saldo(nome):
    if nome in clientes:
        print "Cliente: ", nome, "\nConta:\tSaldo:"
        for conta in clientes[nome]:
            print conta,"\t", clientes[nome][conta][1]
    else:
        print "Erro: Nome de cliente inválido."

