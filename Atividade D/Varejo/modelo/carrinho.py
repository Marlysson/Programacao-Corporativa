# -*- coding:utf8 -*-

class Carrinho(object):
	def __init__(self):
		self._produtos = list()

	@property
	def count_produtos(self):
		return len(self._produtos)
		
	def add_produto(self,produto):
		self._produtos.append(produto)

	def __repr__(self):
		return "{}".format(self._produtos)