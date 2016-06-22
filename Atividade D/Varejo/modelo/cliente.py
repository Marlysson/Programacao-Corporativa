# -*- coding: utf-8 -*-

class Cliente(object):
	def __init__(self,nome):
		self._nome   = nome.lower().capitalize()
		self._pontos = 0

	@property
	def nome(self):
		return self._nome

	@property
	def pontos(self):
		return self._pontos

	@pontos.setter
	def pontos(self,pontos):
		self._pontos = pontos

	def __add__(self,pontos):
		self._pontos += pontos
	
	def __repr__(self):
		return "{} , {} pontos".format(self.nome,self.pontos)
