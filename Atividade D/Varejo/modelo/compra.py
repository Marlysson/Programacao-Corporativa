# -*- coding: utf8 -*-
import sys,os

#Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from cliente import Cliente
from carrinho import Carrinho
from produto import Produto
from regras_negocio.pontos_cliente import Mais1000Pontos

class Compra(object):

	def __init__(self,cliente,carrinho):
		self._cliente = cliente
		self._carrinho = carrinho
		self._descontos = list()
		self._total = 0

	@property
	def cliente(self):
		return self._cliente

	@property
	def descontos(self):
		return self._descontos

	@property
	def total(self):
		return self._total

	@total.setter
	def total(self,valor):
		self._total = valor

	def calcula_total(self):
		preco_total = 0.0

		produtos_contabilizados = []

		for item in self.carrinho.produtos:

			if item.nome not in produtos_contabilizados:

				quantidade = self.carrinho.count_produto(item.nome)
				preco = item.preco

				produtos_contabilizados.append(item.nome)

				preco_total += quantidade * preco

		return preco_total

	def add_desconto(self,desconto):
		self._descontos.append(desconto)

	def aplicar_descontos(self):
		for desconto in self.descontos:
			self.total = self.calcula_total() - desconto.descontar(self)

# produto1 = Produto("Arroz",5)
# produto2 = Produto("Arroz",5)
# produto3 = Produto("Feijão",5)
# produto4 = Produto("Refrigerante",5)

# cliente = Cliente("Marlysson")
# cliente.pontos = 2000

# carrinho = Carrinho()

# for produto in [produto1,produto2,produto3,produto4]:
# 	carrinho.add_produto(produto)

# compra = Compra(cliente,carrinho)

# compra.add_desconto(Mais1000Pontos())
# compra.aplicar_descontos()

print(compra.total)
print(cliente.pontos)