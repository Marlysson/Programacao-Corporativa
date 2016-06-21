# -*- coding: utf8 -*-

class Produto(object):
	def __init__(self,nome,preco):
		self._nome = nome.lower().capitalize()
		self._preco = preco

	@property
	def nome(self):
		return self._nome

	@property
	def preco(self):
		return self._preco

	@nome.getter
	def nome(self):
		return self._nome

	@preco.getter
	def preco(self):
		return self._preco

	def __repr__(self):
		return "Produto({}, R${:.2f})".format(self._nome,self._preco)
