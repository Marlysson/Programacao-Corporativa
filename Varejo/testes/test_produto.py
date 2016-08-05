# -*- coding:utf-8 -*-

import unittest
import sys,os

#Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from modelo.produto import Produto

class TestaProduto(unittest.TestCase):

	def setUp(self):
		self.produto = Produto("Feijão",5.6)

	def test_e_instancia(self):
		self.assertIsInstance(self.produto,type(self.produto))

	def test_nome_produto(self):
		self.assertEqual(self.produto.nome,"Feijão")

	def test_preco_produto(self):
		self.assertEqual(self.produto.preco,5.60)

	def test_preco_errado(self):
		self.assertNotEqual(self.produto.preco,5)

	def test_representacao_produto(self):
		self.assertEqual(str(self.produto),"Produto(Feijão, R$5.60)")


if __name__ == "__main__":
	unittest.main()