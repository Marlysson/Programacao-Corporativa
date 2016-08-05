# -*- coding:utf-8 -*-

import unittest
import sys,os

#Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from modelo.compra import Compra
from modelo.carrinho import Carrinho
from modelo.cliente import Cliente
from modelo.produto import Produto
from regras_negocio.fidelidade_pontos import Fidelidade1000Pontos
from regras_negocio.compra_cara import ValorMaior1000Reais

class TestCompra(unittest.TestCase):

	def test_e_instancia(self):
		compra = Compra(None,None)

		self.assertIsInstance(compra,type(Compra(None,None)))
	
	def test_nome_cliente_da_compra(self):

		cliente = Cliente("Marlysson")
		cliente.pontos = 2000

		carrinho = Carrinho()

		compra = Compra(cliente,carrinho)

		self.assertEqual(compra.cliente.nome,"Marlysson")

	def test_pontos_cliente_da_compra(self):
		
		cliente = Cliente("Marlysson")
		cliente.pontos = 1500

		carrinho = Carrinho()

		compra = Compra(cliente,carrinho)

		self.assertEqual(compra.cliente.pontos,1500)

	def test_quantidade_descontos(self):
		
		cliente = Cliente("Marlysson")

		carrinho = Carrinho()

		compra = Compra(cliente,carrinho)
		compra.add_desconto(ValorMaior1000Reais())

		self.assertEqual(len(compra.descontos),1)

	def test_desconto_por_pontos_cliente(self):

		produto1 = Produto("Arroz",5)
		produto2 = Produto("Arroz",5)
		produto3 = Produto("Feijão",5)
		produto4 = Produto("Refrigerante",5)

		cliente = Cliente("Marlysson")
		cliente.pontos = 2000

		carrinho = Carrinho()

		for produto in [produto1,produto2,produto3,produto4]:
			carrinho.add_produto(produto)

		compra = Compra(cliente,carrinho)

		compra.add_desconto(Fidelidade1000Pontos())

		compra.aplicar_descontos()

		self.assertEqual(compra.total,19.00)

	def test_desconto_por_valor_da_compra(self):

		produto1 = Produto("Bicicleta",500)
		produto2 = Produto("Fogão",600)

		cliente = Cliente("Marlysson")

		carrinho = Carrinho()

		for produto in [produto1,produto2]:
			carrinho.add_produto(produto)

		compra = Compra(cliente,carrinho)

		compra.add_desconto(ValorMaior1000Reais())

		compra.aplicar_descontos()

		self.assertEqual(compra.total,990.0)

if __name__ == "__main__":
	unittest.main()