# -*- coding: utf-8 -*_

import unittest
import sys,os

# Adicionando pasta externa para capturar os modelos
pasta_projeto = os.path.abspath("../")
sys.path.append(pasta_projeto)

from modelo.cliente import Cliente

class TestaCliente(unittest.TestCase):

	def test_nome_cliente(self):

		self.cliente = Cliente("Marlysson")

		self.assertEqual(self.cliente.nome,"Marlysson")

	def test_pontos_cliente(self):
		self.cliente = Cliente("Marlysson")
		self.cliente.pontos = 10

		self.assertEqual(self.cliente.pontos,10)

	def test_soma_pontos_cliente(self):
		self.cliente = Cliente("Marcelo")

		self.cliente.pontos = 5
		self.cliente.pontos += 10

		self.assertEqual(self.cliente.pontos,15)

if __name__ == "__main__":
	unittest.main()