# -*- coding:utf-8 -*-

import unittest
import sys,os

#Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from modelo.produto import Produto
from modelo.carrinho import Carrinho

class TestaCarrinho(unittest.TestCase):

	def test_e_instancia(self):
		carrinho = Carrinho()

		self.assertIsInstance(carrinho,type(Carrinho()))

	def test_representacao_carrinho_vazia(self):
		carrinho = Carrinho()

		self.assertEqual(str(carrinho),"[]")

	def test_quant_produtos(self):
		carrinho = Carrinho()

		self.assertEqual(carrinho.count_produtos,0)

	def test_quantidade_produtos_adicionados(self):

		produto1 = Produto("Arroz",5.6)
		produto2 = Produto("Feijão",4.5)

		carrinho = Carrinho()

		carrinho.add_produto(produto1)
		carrinho.add_produto(produto2)

		self.assertEqual(carrinho.count_produtos,2)

	def test_quantidade_errada_produto(self):
		carrinho = Carrinho()

		self.assertNotEqual(carrinho.count_produtos,4)
	
	def test_representacao_carrinho_com_itens(self):
		produto = Produto("Arroz",5.6)
		carrinho = Carrinho()

		carrinho.add_produto(produto)

		self.assertEqual(str(carrinho),"[Produto(Arroz, R$5.60)]")

	def test_tipo_retorno_dicionario_de_produtos(self):
		produto1 = Produto("Arroz",5.6)
		produto2 = Produto("Arroz",5.6)
		produto3 = Produto("Feijão",4)
		produto4 = Produto("Refrigerante",7.00)

		carrinho = Carrinho()

		for produto in [produto1,produto2,produto3,produto4]:
			carrinho.add_produto(produto)

		self.assertEqual(type(carrinho.detalhes()),dict)

	def test_quantidade_determinado_produto(self):
		
		produto1 = Produto("Arroz",5.6)
		produto2 = Produto("Arroz",5.6)
		produto3 = Produto("Feijão",4)
		produto4 = Produto("Refrigerante",7.00)
		produto5 = Produto("Refrigerante",7.00)

		carrinho = Carrinho()

		for produto in [produto1,produto2,produto3,produto4,produto5]:
			carrinho.add_produto(produto)

		self.assertEqual(carrinho.count_produto(produto1),2)

if __name__ == "__main__":
	unittest.main()