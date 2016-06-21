# -*- coding: utf-8 -*-

class Cliente(object):
	def __init__(self,nome):
		self.nome   = nome.lower().capitalize()
		self.pontos = 0

	def __repr__(self):
		return "{} , {} pontos".format(self.nome,self.pontos)

