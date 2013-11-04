#! /usr/bin/env python
# coding: utf-8

import pickle

class Historico:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        try:
            self.disciplinas = pickle.load(file(self.nome_arquivo, "r"))
        except:
            self.disciplinas = {}
    
    def adicionar_disciplina(self, codigo, nome, creditos, nota):
        if codigo and nome and type(nota) == float and type(creditos) == int:
            self.disciplinas[str(codigo).upper()] = (nome,
                                                     int(creditos),
                                                     float(nota))
    
    def listar_disciplinas(self):
        for materia in self.disciplinas:
            print "[%s] %s - %.2f (x%s)" % (materia,
                                          self.disciplinas[materia][0],
                                          self.disciplinas[materia][2],
                                          self.disciplinas[materia][1])

    def calcular_cra(self):
        soma_nota = soma_creditos = 0
        for materia in self.disciplinas:
            soma_nota += self.disciplinas[materia][2]*self.disciplinas[materia][1]
            soma_creditos += self.disciplinas[materia][1]
        return soma_nota/soma_creditos
    
    def salvar(self):
        pickle.dump(self.disciplinas, file(self.nome_arquivo, "w"))
 
