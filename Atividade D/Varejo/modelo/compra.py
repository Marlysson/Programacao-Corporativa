# -*- coding: utf8 -*-

from cliente import Cliente
from carrinho import Carrinho
from produto import Produto

class Compra(object):

	def __init__(self,cliente):
		self._cliente = cliente
		self._carrinho = Carrinho()
		self._descontos = list()

	@property
	def cliente(self):
		return self._cliente

	@property
	def carrinho(self):
		return self._carrinho