# -*- coding:utf8 -*-

class Carrinho(object):
	def __init__(self):
		self._produtos = list()

	@property
	def count_produtos(self):
		return len(self._produtos)		

	def detalhes(self):
		info_produtos = {}

		for produto in self._produtos:

			nome = produto.nome.lower()

			if nome in info_produtos:
				info_produtos[nome] += 1
			else:
				info_produtos[nome] = 1

		return info_produtos

	def count_produto(self,produto):
		nome_produto = produto.nome.lower()

		return self.detalhes().get(nome_produto,0)
		
	def add_produto(self,produto):
		self._produtos.append(produto)

	def __repr__(self):
		return "{}".format(self._produtos)

# produto1 = Produto("Arroz",5.6)
# produto2 = Produto("Arroz",5.6)
# produto3 = Produto("Feijão",4)
# produto4 = Produto("Refrigerante",7.00)

# carrinho = Carrinho()

# for produto in [produto1,produto2,produto3,produto4]:
# 	carrinho.add_produto(produto)

# print(carrinho.detalhes())